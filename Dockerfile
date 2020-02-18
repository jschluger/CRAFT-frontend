FROM python:3.7.6-slim

WORKDIR /frontend

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /frontend

ENTRYPOINT ["python", "run.py"]