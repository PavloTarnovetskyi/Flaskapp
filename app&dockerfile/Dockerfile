FROM python:3.11-rc-alpine

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
    && pip install boto3

EXPOSE 5000

CMD ["python3", "app.py"]