#!/bin/sh
if [ $ENV -eq "prod" ]
then
    export TOKEN=$(cat /run/secrets/token_discord_bot) && pipenv install  --system --deploy --ignore-pipfile && python main.py
else
    pipenv install  --system --deploy --ignore-pipfile && python main.py
fi
