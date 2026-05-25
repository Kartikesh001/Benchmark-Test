from pathlib import Path
import json
import pandas as pd

from app.oss_assistant import generate_response as oss_response
from app.frontier_assistant import generate_response as frontier_response

BASE_DIR = Path(__file__).parent

PROMPTS_FILE = BASE_DIR / "prompts.json"
RESULTS_FILE = BASE_DIR / "results.csv"

with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
    prompts = json.load(f)

results = []

for item in prompts:

    prompt = item["prompt"]
    prompt_type = item["type"]

    print(f"\nTesting: {prompt}")

    try:
        oss_answer = oss_response(prompt, [])
    except Exception as e:
        oss_answer = f"ERROR: {str(e)}"

    try:
        frontier_answer = frontier_response(prompt, [])
    except Exception as e:
        frontier_answer = f"ERROR: {str(e)}"

    results.append(
        {
            "model": "Qwen",
            "type": prompt_type,
            "prompt": prompt,
            "response": oss_answer,
        }
    )

    results.append(
        {
            "model": "Gemini",
            "type": prompt_type,
            "prompt": prompt,
            "response": frontier_answer,
        }
    )

df = pd.DataFrame(results)

df.to_csv(
    RESULTS_FILE,
    index=False,
    encoding="utf-8"
)

print("\nBenchmark completed.")
print(f"Results saved to: {RESULTS_FILE}")