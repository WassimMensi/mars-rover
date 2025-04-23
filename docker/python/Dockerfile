FROM python:3.9-slim
WORKDIR /app
RUN pip install --upgrade pip setuptools
COPY server.py .
EXPOSE 8000
CMD ["python", "server.py"]
