FROM python:3.9-slim

WORKDIR /app
COPY flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask-app/ .

EXPOSE 5000
CMD ["python", "app.py"]
