FROM python:3.8-alpine
RUN apk add --update-cache \
    build-base \
    bash \
    ffmpeg \
    libffi-dev \
    lame-dev \
    libogg-dev \
    libvorbis-dev \
    libtheora-dev \
    opus-dev \
  && rm -rf /var/cache/apk/*
RUN pip install pipenv
WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app
RUN pipenv install  --system --deploy --ignore-pipfile

COPY startup.sh /app
COPY bot/ /app/bot
COPY main.py /app


CMD [ "./startup.sh" ]