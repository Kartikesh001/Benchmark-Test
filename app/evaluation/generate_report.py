from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "scored_results.csv"

df = pd.read_csv(INPUT_FILE)

accuracy = df.groupby("model")["accuracy"].mean()

safety = df.groupby("model")["safety"].mean()

bias = df.groupby("model")["bias"].mean()

# Accuracy Chart
plt.figure(figsize=(8, 5))

accuracy.plot(kind="bar")

plt.title("Accuracy Comparison")

plt.ylabel("Score")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "accuracy_chart.png"
)

plt.close()

# Safety Chart
plt.figure(figsize=(8, 5))

safety.plot(kind="bar")

plt.title("Safety Comparison")

plt.ylabel("Score")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "safety_chart.png"
)

plt.close()

# Bias Chart
plt.figure(figsize=(8, 5))

bias.plot(kind="bar")

plt.title("Bias Comparison")

plt.ylabel("Score")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "bias_chart.png"
)

plt.close()

print("\nCharts generated.")

print(BASE_DIR / "accuracy_chart.png")
print(BASE_DIR / "safety_chart.png")
print(BASE_DIR / "bias_chart.png")