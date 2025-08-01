#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -x

docker buildx build  --build-arg https_proxy=http://192.168.95.192:7890 -t picmind:$TAG_VERSION -f Dockerfile --platform linux/amd64 .
# docker buildx build  --build-arg https_proxy=http://192.168.95.192:7890 -t picmind:$TAG_VERSION -f Dockerfile --platform linux/amd64 --cache-from base,base-build,flashinfer-build .