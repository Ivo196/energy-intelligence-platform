@echo off
cd /d "%~dp0"
python -m streamlit run dashboard/dashboard.py --server.port=8501 --server.headless=true
