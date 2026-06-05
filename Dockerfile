# ---------------------------------------------------------------
# Dockerfile — Energy Intelligence Platform 
# ---------------------------------------------------------------
# Build:  docker build -t energy-intelligence-platform .
# Run:    docker run -p 8000:8000 \
#           -v $(pwd)/data:/app/data \
#           --env-file .env \
#           energy-intelligence-platform
# ---------------------------------------------------------------

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]