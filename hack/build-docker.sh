#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

docker buildx build --push -t registry.dev.ai-links.com/ailinks/gpustack:v0.5.4 -f Dockerfile --platform linux/amd64 .