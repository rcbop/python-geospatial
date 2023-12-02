FROM python:3.9-slim

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api /src/api

CMD ["python", "/src/api/main.py"]
