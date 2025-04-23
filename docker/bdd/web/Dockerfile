FROM python:3.11-slim
WORKDIR /app
COPY server.py .
RUN pip install psycopg2-binary
CMD ["python", "server.py"]
