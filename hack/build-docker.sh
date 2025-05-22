#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

docker buildx build --build-arg https_proxy=http://192.168.95.192:7890 --push -t registry.dev.ai-links.com/ailinks/gpustack:v0.6.0 -f Dockerfile --platform linux/amd64 .