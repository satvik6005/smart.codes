FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y \
curl
COPY testing.py testing.py
COPY requirements.txt requirements.txt
COPY testing.sh testing.sh
RUN pip install -r requirements.txt
