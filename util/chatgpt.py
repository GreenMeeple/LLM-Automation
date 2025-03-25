import csv
import os
from data.jailbreak import long_DAN, tasks
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_chatgpt(debug, version):
    response_path = "../Data/Responses_LLM/chatgpt.csv"
    os.makedirs(os.path.dirname(response_path), exist_ok=True)

    model_name = "gpt-3.5-turbo" if version == 3 else "gpt-4o-mini"

    with open(response_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["prompt", "response"])
        writer.writeheader()

        for task in tasks:
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": long_DAN},
                        {"role": "user", "content": task}
                    ],
                    temperature=0.6
                )

                content = response.choices[0].message.content
                writer.writerow({
                    "prompt": task,
                    "response": content
                })
                print(f"Prompt: {task}\nResponse: {content}\n")

            except Exception as e:
                print(f"Error on task: {task}\n{e}")

    print("✅ Results saved to chatgpt.csv")
