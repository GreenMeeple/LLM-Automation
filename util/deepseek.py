import requests
import csv
import os
from data.jailbreak import long_DAN, tasks, tasks_debug

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
model_name = "deepseek-r1:7b"

def run_deepseek(debug):
    # Open a CSV file to write
    response_path = "../Data/Responses_LLM/deepseek.csv"
    os.makedirs(os.path.dirname(response_path), exist_ok=True) # check if directory exists

    with open(response_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["prompt", "response"])
        writer.writeheader()

        # Loop through each task
        task_list = tasks_debug if debug else tasks

        for task in task_list:
            response = requests.post(OLLAMA_URL, json={
                "model": model_name,
                "system": long_DAN,
                "prompt": task,
                "temperature": 0.6,
                "max_tokens": -1,
                "stream": False
            })

            output = response.json()
            writer.writerow({
                "prompt": task,
                "response": output.get("response", "")
            })
            print(f"{task} has been answered.")

    print("✅ Results saved to Data/Responses_LLM/deepseek.csv")
