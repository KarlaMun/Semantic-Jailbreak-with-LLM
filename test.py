from transformers import LlamaTokenizer, LlamaForCausalLM
import torch

# Use the Llama-specific tokenizer and model
model_name = "lmsys/vicuna-7b-v1.5"
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).cuda()

# Tokenize input
prompt = "What is the capital of France?"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate output
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=100)

# Decode and print the output
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)
