#!/bin/bash
if [ $ENV = "prod" ]; then
    export TOKEN=$(cat /run/secrets/token_discord_bot) && python main.py
else
    python main.py
fi
