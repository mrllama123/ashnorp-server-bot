FROM python:3.8-alpine
RUN apk add --update-cache \
    build-base \
    bash \
    ffmpeg \
  && rm -rf /var/cache/apk/*
RUN pip install pipenv
WORKDIR /app
COPY bot/ /app/bot
COPY main.py /app
COPY Pipfile /app
COPY Pipfile.lock /app
COPY startup.sh /app

CMD [ "./startup.sh" ]