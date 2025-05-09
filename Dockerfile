FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "ui.py", "--server.port=8080", "--server.headless=true", "--server.address=0.0.0.0"]
