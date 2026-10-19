"""Run once in the same environment as the notebook; writes environment.txt with exact versions."""
import sys, importlib
mods = ["numpy", "pandas", "scipy", "sklearn", "xgboost", "lightgbm", "catboost", "shap", "lime", "matplotlib", "openpyxl"]
lines = [f"python {sys.version.split()[0]}"]
for m in mods:
    try:
        lines.append(f"{m} {importlib.import_module(m).__version__}")
    except Exception as e:
        lines.append(f"{m} not installed ({e.__class__.__name__})")
open("environment.txt", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
