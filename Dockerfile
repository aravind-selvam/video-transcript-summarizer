FROM python:3.10-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt update -y && apt-get install git -y && apt install ffmpeg -y && pip install -r requirements.txt

CMD ["python3", "app.py"]