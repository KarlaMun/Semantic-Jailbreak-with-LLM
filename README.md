# Semantic-Jailbreak-with-LLM

This project explores semantic jailbreaking techniques to bypass or extend the capabilities of Language Models (LLMs) by manipulating the input in a way that the model interprets differently from its intended design constraints. By leveraging this approach, the project aims to analyze, document, and potentially mitigate jailbreaking tactics on language models.


## Introduction
Language models are increasingly integrated into various applications, yet they can be susceptible to "jailbreak" attempts where input manipulation forces the model to bypass its constraints. This project investigates semantic methods for jailbreaking, contributing to both the understanding and potential mitigation of such vulnerabilities. By understanding how models interpret language differently from expectations, we aim to provide a framework to enhance LLM safety and robustness.

## Framework installation

Log into a linux machine with Anaconda installed.

In the terminal do:
1. Clone the repository:
  ```
  git clone git@github.com:KarlaMun/Semantic-Jailbreak-with-LLM.git
  ```
2. Access the code:
  ```
  cd Semantic-Jailbreak-with-LLM
  ```

3. Install the conda enviroment:
  ```
  conda env create -f config.yml
  conda activate llm-env
  conda develop .
  ```
  
3.1 Update the conda enviroment:
   ```
   conda env update --file config.yml --prune
   ```

## Features
Semantic Jailbreak Methods: Techniques for crafting inputs that bypass LLM safeguards. \
Analysis of Model Responses: Tools to evaluate the LLM's output in response to jailbreaking attempts.

## License
This project is licensed under the MIT License.
