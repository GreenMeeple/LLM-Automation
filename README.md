# LLM-Automation

> This Repository is a seperately version of the project [LLM-Powered-App-Challenges](https://github.com/GreenMeeple/LLM-Powered-Apps-Challenges)

## Overview

This project is designed to automate the process of prompting and collecting responses from large language models (LLMs), either locally via Ollama or remotely via the OpenAI API. It's tailored for tasks like jailbreak testing, prompt evaluation, and LLM behavior analysis.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ , `pip` for installing packages

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/LLM-Automation.git
    cd LLM-App-Automation
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## 🧭 Usage

### Run with Local DeepSeek (Ollama)

Make sure [Ollama](https://ollama.com/) is installed and running.

1. Download the DeepSeek model: `ollama run deepseek-r1:7b`

    You can also try other variants depending on your use case.

2. Run the script: `python main.py --model deepseek`

This will:

- Load prompts from `data/jailbreak.py`
- Send them to the DeepSeek model running locally via Ollama
- Save the results to `Data/Responses_LLM/deepseek.csv`

### ChatGPT API

The project includes functionality to send prompts to OpenAI’s ChatGPT models (gpt-3.5-turbo, gpt-4o, etc.).

> ❌ **Notice:**  We did not use ChatGPT in this project because OpenAI API requires a paid plan, and free-tier accounts do not have API access — even to GPT-3.5.

If you'd like to use ChatGPT anyway, you'll need to:

Add your API key to a .env file: `OPENAI_API_KEY=your-key-here`

Run with: `python main.py --model chatgpt --version 4`

## 🗃️ Project Details

### Task Management

Prompts/tasks are stored in `data/jailbreak.py`. You can modify or expand:

- **long_DAN**: a system prompt for jailbreak-style prompting
- **tasks**: your actual prompt list
- **tasks_debug**: a shorter debug version

### Outputs

All responses are saved to: `Data/Responses_LLM/<model>.csv`

Each CSV contains:

- **prompt**: the task prompt sent to the model
- **response**: the model's reply

## 📦 Project Structure (Partial)

```bash
LLMAutomation/
├── data/
│   └── jailbreak.py         # Contains prompts like long_DAN and task sets
├── llm/
│   ├── deepseek.py          # Logic for interacting with DeepSeek via Ollama
│   └── chatgpt.py           # Logic for interacting with OpenAI's ChatGPT API
├── main.py                  # Entry point, CLI-driven
└── Data/Responses_LLM/      # Where CSV responses are saved
```
