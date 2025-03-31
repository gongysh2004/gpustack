ARG CUDA_VERSION=12.4.1

FROM ngc.nju.edu.cn/nvidia/cuda:$CUDA_VERSION-cudnn-runtime-ubuntu22.04

ARG TARGETPLATFORM
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    tzdata \
    iproute2 \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . /workspace/gpustack
# COPY hack/pip.conf ~/.config/pip/pip.conf
RUN --mount=type=bind,source=./hack/pip.conf,target=/root/.config/pip/pip.conf \
    cd /workspace/gpustack && \
    make build

RUN --mount=type=bind,source=./hack/pip.conf,target=/root/.config/pip/pip.conf \
    if [ "$TARGETPLATFORM" = "linux/amd64" ]; then \
    # Install vllm dependencies for x86_6d4
    WHEEL_PACKAGE="$(ls /workspace/gpustack/dist/*.whl)[all]"; \
    else  \
    WHEEL_PACKAGE="$(ls /workspace/gpustack/dist/*.whl)[audio]"; \
    fi && \
    pip install pipx && \
    pip install $WHEEL_PACKAGE && \
    pip cache purge && \
    rm -rf /workspace/gpustack
    
RUN gpustack download-tools

ENTRYPOINT [ "gpustack", "start" ]
