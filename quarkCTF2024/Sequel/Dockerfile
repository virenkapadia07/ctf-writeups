FROM python:3.10.13-slim-bullseye

WORKDIR /app

RUN pip install flask

COPY . .

CMD gunicorn -b 0.0.0.0:80 sqli_chal:app
EXPOSE 80
