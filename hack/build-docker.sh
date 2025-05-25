#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -x

docker buildx build --build-arg VERSION=$VERSION  --target ${TARGET:-final} --build-arg https_proxy=http://192.168.95.192:7890 --push -t registry.dev.ai-links.com/ailinks/gpustack:$VERSION -f Dockerfile --platform linux/amd64 .