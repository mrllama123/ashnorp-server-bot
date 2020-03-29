#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Needs  the commit tag version added"
    exit 1
fi
version_tag=$1 

# enable buildx mode
export DOCKER_CLI_EXPERIMENTAL=enabled

# build image
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t test-discord-bot:latest .

# tag image
docker tag test-discord-bot:latest mrllama12/test-discord-bot:latest
docker tag mrllama12/test-discord-bot:latest mrllama12/test-discord-bot:$version_tag

docker push mrllama12/test-discord-bot:latest
docker push mrllama12/test-discord-bot:latest mrllama12/test-discord-bot:$version_tag
# push image
# docker push --disable-content-trust 192.168.1.22:5000/test-discord-bot:latest
# docker push --disable-content-trust 192.168.1.22:5000/test-discord-bot:$version_tag 