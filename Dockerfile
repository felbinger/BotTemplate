FROM python:3.9-alpine

ENV DB_HOST=mariadb \
    DB_PORT=3306 \
    DB_USER=bot \
    DB_DATABASE=bot

RUN apk update \
 && apk add gcc musl-dev

WORKDIR /usr/src

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app /usr/src/app
COPY translations /usr/src/translations

RUN addgroup -g 1000 bot \
 && adduser -G bot -u 1000 -s /bin/sh -D -H bot

USER bot

CMD python /usr/src/app/start.py
