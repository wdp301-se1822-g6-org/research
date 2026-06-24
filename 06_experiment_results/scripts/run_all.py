"""Reproduce all experiments end-to-end. Run: python scripts/run_all.py"""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = [
    "e3_generate_dataset.py", "e3_train_models.py",
    "e2_generate_survey.py", "e2_analyze_survey.py",
    "e1_chatbot_eval.py",
]
for s in STEPS:
    print(f"\n{'='*60}\nRunning {s}\n{'='*60}")
    subprocess.run([sys.executable, str(HERE / s)], check=True)
print("\nAll experiments completed.")
