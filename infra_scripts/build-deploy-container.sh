#!/bin/bash

version_tag=$(git describe --abbrev=0 --tags)

# enable buildx mode
export DOCKER_CLI_EXPERIMENTAL=enabled
docker login
# build image and push it up
docker buildx build --platform linux/amd64,linux/arm/v7 -t mrllama12/test-discord-bot:latest -t mrllama12/test-discord-bot:$version_tag --push .

