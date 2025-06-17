# 离线安装

你可以在离线环境中安装 aiMindServe 将在无网络连接的情况下安装。

以下是在离线环境中安装 aiMindServe 的可用方法：

| 操作系统 | 架构           | 支持的安装方式                                                                                                                         |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Linux    | AMD64<br>ARM64 | [Docker 安装](#docker-安装)（推荐）|

## 前置条件

- [端口要求](../installation-requirements.md#端口要求)
- NVIDIA GPU（需支持 CUDA）

=== "Linux"

    检查 NVIDIA GPU 是否支持：

    ```bash
    nvidia-smi
    ```

## Docker 安装

### 前置条件

- [Docker](https://docs.docker.com/engine/install/)

### 运行 aiMindServe

使用 Docker 运行 aiMindServe 时，只要 Docker 镜像可用，即可在离线环境中直接使用。请按以下步骤操作：

1. 在在线环境中拉取 aiMindServe docker 镜像：

```bash
docker pull gpustack/gpustack:latest-nvidia-cuda
```

如果在线环境与离线环境在操作系统或架构上不同，请在拉取镜像时指定离线环境的操作系统和架构：

```bash
docker pull --platform linux/amd64 gpustack/gpustack:latest-nvidia-cuda
```

2. 将 docker 镜像发布到私有仓库或直接加载到离线环境中。
3. 参考 [Docker 安装](./online-installation.md#docker-安装) 指南使用 Docker 运行 GPUStack。

 