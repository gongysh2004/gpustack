# 离线安装

你可以在离线环境中安装 GPUStack。离线环境指的是 GPUStack 将在无网络连接的情况下安装。

以下是在离线环境中安装 GPUStack 的可用方法：

| 操作系统 | 架构           | 支持的安装方式                                                                                                                         |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Linux    | AMD64<br>ARM64 | [Docker 安装](#docker-安装)（推荐）<br>[pip 安装](#pip-安装)           |
| Windows  | AMD64<br>ARM64 | [pip 安装](#pip-安装)                                                 |

## 前置条件

- [端口要求](../installation-requirements.md#端口要求)
- Moore Threads GPU（需支持 Moore Threads MUSA）

=== "Linux"

    检查 Moore Threads GPU 是否支持：

    ```bash
    musa-smi
    ```

=== "Windows"

    Windows 用户需手动验证是否支持上述指令。

## Docker 安装

### 前置条件

- [Docker](https://docs.docker.com/engine/install/)

### 运行 GPUStack

使用 Docker 运行 GPUStack 时，只要 Docker 镜像可用，即可在离线环境中直接使用。请按以下步骤操作：

1. 在在线环境中拉取 GPUStack docker 镜像：

```bash
docker pull gpustack/gpustack:latest-moorethreads-musa
```

如果在线环境与离线环境在操作系统或架构上不同，请在拉取镜像时指定离线环境的操作系统和架构：

```bash
docker pull --platform linux/amd64 gpustack/gpustack:latest-moorethreads-musa
```

2. 将 docker 镜像发布到私有仓库或直接加载到离线环境中。
3. 参考 [Docker 安装](./online-installation.md#docker-安装) 指南使用 Docker 运行 GPUStack。

## pip 安装

### 前置条件

- Python 3.10 ~ 3.12

检查 Python 版本：

```bash
python -V
```

### 安装 GPUStack

对于手动 pip 安装，你需要在在线环境中准备所需的包和工具，然后将其传输到离线环境中。

在在线环境中设置与离线环境相同的环境，包括**操作系统**、**架构**和 **Python 版本**。

#### 步骤 1：下载所需包

在在线环境中运行以下命令：

=== "Linux"

    ```bash
    PACKAGE_SPEC="gpustack[audio]"
    # 安装特定版本
    # PACKAGE_SPEC="gpustack[audio]==0.6.0"
    ```

    如无需音频模型支持，可直接设置：

    ```bash
    PACKAGE_SPEC="gpustack"
    ```

=== "Windows"

    ```powershell
    $PACKAGE_SPEC = "gpustack[audio]"
    # 安装特定版本
    # $PACKAGE_SPEC = "gpustack[audio]==0.6.0"
    ```

    如无需音频模型支持，可直接设置：

    ```powershell
    $PACKAGE_SPEC = "gpustack"
    ```

下载所有所需包：

```bash
pip wheel $PACKAGE_SPEC -w gpustack_offline_packages
```

安装 GPUStack 以使用其 CLI：

```bash
pip install gpustack
```

下载依赖工具并保存为归档文件：

```bash
gpustack download-tools --save-archive gpustack_offline_tools.tar.gz
```

如果在线环境与离线环境不同，请明确指定**操作系统**、**架构**和**设备**：

```bash
gpustack download-tools --save-archive gpustack_offline_tools.tar.gz --system linux --arch amd64 --device moorethreads-musa
```

#### 步骤 2：传输包

将以下文件从在线环境传输到离线环境：

- `gpustack_offline_packages` 目录。
- `gpustack_offline_tools.tar.gz` 文件。

#### 步骤 3：安装 GPUStack

在离线环境中运行以下命令：

```bash
# 从下载的包中安装 GPUStack
pip install --no-index --find-links=gpustack_offline_packages gpustack

# 加载并应用预下载的工具归档
gpustack download-tools --load-archive gpustack_offline_tools.tar.gz
```

现在你可以按照 [pip 安装](online-installation.md#pip-安装) 指南运行 GPUStack。 