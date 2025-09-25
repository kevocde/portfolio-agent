#!/bin/bash

# Check if image name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <image_name>"
    echo "Example: $0 my-app"
    exit 1
fi

BUILD_ARGS=""
while IFS='=' read -r key value; do
	if [[ ! -z "$key" && ! "$key" =~ ^# ]]; then
		BUILD_ARGS+="--build-arg $key=$value "
	fi
done < .env

command="docker build $BUILD_ARGS-t $1 ."

eval $command