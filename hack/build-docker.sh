#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

docker buildx build --load -t ailinks/gpustack:v0.5.1 -f Dockerfile --platform linux/amd64 .