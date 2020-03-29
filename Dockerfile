FROM python:3.8-alpine
RUN apk add --update-cache \
    build-base \
  && rm -rf /var/cache/apk/*
RUN pip install pipenv
WORKDIR /app
COPY bot /app
COPY main.py /app

CMD [ "./startup.sh" ]