"""
upload_to_hf.py
---------------
Uploads code, models, and data files to the Hugging Face Space.
Run from the project root after any local update.

Usage:
    python upload_to_hf.py
"""

from huggingface_hub import HfApi
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────
HF_REPO_ID = "bachirij/energy-intelligence-platform"
REPO_TYPE  = "space"
LOCAL_ROOT = Path(__file__).resolve().parent
# ───────────────────────────────────────────────────────────────

api = HfApi()

# 1. Source code
print("Uploading source code...")
for folder in ["dashboard", "src"]:
    api.upload_folder(
        folder_path=str(LOCAL_ROOT / folder),
        path_in_repo=folder,
        repo_id=HF_REPO_ID,
        repo_type=REPO_TYPE,
    )

# 2. Root files
print("Uploading root files...")
for filename in ["app.py", "requirements.txt", "Dockerfile"]:
    api.upload_file(
        path_or_fileobj=str(LOCAL_ROOT / filename),
        path_in_repo=filename,
        repo_id=HF_REPO_ID,
        repo_type=REPO_TYPE,
    )

# 3. Models
print("Uploading models...")
api.upload_folder(
    folder_path=str(LOCAL_ROOT / "models"),
    path_in_repo="models",
    repo_id=HF_REPO_ID,
    repo_type=REPO_TYPE,
)

# 4. Data
print("Uploading data files...")

api.upload_file(
    path_or_fileobj=str(LOCAL_ROOT / "data/realtime/country=FR/realtime.parquet"),
    path_in_repo="data/realtime/country=FR/realtime.parquet",
    repo_id=HF_REPO_ID,
    repo_type=REPO_TYPE,
)

for year in [2024, 2026]:
    folder = LOCAL_ROOT / f"data/featured/country=FR/year={year}"
    for parquet_file in folder.glob("*.parquet"):
        api.upload_file(
            path_or_fileobj=str(parquet_file),
            path_in_repo=f"data/featured/country=FR/year={year}/{parquet_file.name}",
            repo_id=HF_REPO_ID,
            repo_type=REPO_TYPE,
        )

monitoring_dir = LOCAL_ROOT / "data/monitoring"
latest_report = sorted(monitoring_dir.glob("*.json"))[-1]
api.upload_file(
    path_or_fileobj=str(latest_report),
    path_in_repo=f"data/monitoring/{latest_report.name}",
    repo_id=HF_REPO_ID,
    repo_type=REPO_TYPE,
)

print("\nDone. Visit your Space at:")
print(f"  https://huggingface.co/spaces/{HF_REPO_ID}")