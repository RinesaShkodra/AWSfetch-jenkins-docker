FROM python:3.8-slim-buster
RUN pip install boto3
WORKDIR /app
COPY . .

CMD ["python3", "EC2Fetcher.py"]





