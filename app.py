# app.py
# Entry point for Hugging Face Spaces (Docker + Streamlit).
import runpy
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / "dashboard"))

runpy.run_path(
    str(root / "dashboard" / "dashboard.py"),
    run_name="__main__",
)