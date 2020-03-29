#!/bin/bash

version_tag=$(git describe --abbrev=0 --tags)

# enable buildx mode
export DOCKER_CLI_EXPERIMENTAL=enabled
docker login
# build image
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t mrllama12/test-discord-bot:latest -t mrllama12/test-discord-bot:$version_tag --push .

# tag image

# docker login
# docker push mrllama12/test-discord-bot:latest
# docker push mrllama12/test-discord-bot:$version_tag
# push image
# docker push --disable-content-trust 192.168.1.22:5000/test-discord-bot:latest
# docker push --disable-content-trust 192.168.1.22:5000/test-discord-bot:$version_tag 