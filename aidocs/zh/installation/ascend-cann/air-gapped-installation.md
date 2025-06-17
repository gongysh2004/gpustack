# 离线安装

在 GPUStack 中，`llama-box` 和 `vox-box` 后端支持 Ascend CANN 推理。

## 支持的设备

- [x] Ascend GPU（需支持 Ascend CANN）

## 支持的平台

| 操作系统 | 架构           | 支持的安装方式                                                                                                                         |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Linux    | AMD64<br>ARM64 | [Docker 安装](#docker-安装)（推荐）<br>[pip 安装](#pip-安装)           |
| Windows  | AMD64<br>ARM64 | [pip 安装](#pip-安装)                                                 |

## 支持的后端

- [x] llama-box
- [x] vox-box

## 前置条件

- [端口要求](../installation-requirements.md#端口要求)
- Ascend GPU（需支持 Ascend CANN）

=== "Linux"

    检查 Ascend GPU 是否支持：

    ```bash
    npu-smi info
    ```

=== "Windows"

    Windows 用户需手动验证是否支持上述指令。

## Docker 安装

### 前置条件

- [Docker](https://docs.docker.com/engine/install/)

### 运行 GPUStack

1. 在有网络的环境中拉取 Docker 镜像：

```bash
docker pull gpustack/gpustack:latest-ascend-cann
```

2. 将镜像保存为 tar 文件：

```bash
docker save gpustack/gpustack:latest-ascend-cann > gpustack-ascend-cann.tar
```

3. 将 tar 文件传输到离线环境。

4. 在离线环境中加载镜像：

```bash
docker load < gpustack-ascend-cann.tar
```

5. 运行 GPUStack 服务器及内置工作节点（推荐 host 网络模式）：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-ascend-cann
```

如需更改默认服务器端口 80，请使用 `--port` 参数：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-ascend-cann \
    --port 9090
```

如有端口冲突或需自定义启动参数，请参阅 [CLI 参考](../../cli-reference/start.md)。

检查启动日志是否正常：

```bash
docker logs -f gpustack
```

若日志正常，可在浏览器中打开 `http://your_host_ip` 访问 GPUStack UI。使用用户名 `admin` 和默认密码登录。可通过以下命令获取默认密码：

```bash
docker exec -it gpustack cat /var/lib/gpustack/initial_admin_password
```

### （可选）添加工作节点

你可以为 GPUStack 添加更多 Ascend GPU 节点。需在其他 Ascend GPU 节点上添加工作节点，并指定 `--server-url` 和 `--token` 参数加入 GPUStack。

在 GPUStack **服务器节点**上运行以下命令获取 token：

```bash
docker exec -it gpustack cat /var/lib/gpustack/token
```

在工作节点上运行以下命令注册到 GPUStack 服务器（请替换 URL 和 token）：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-ascend-cann \
    --server-url http://your_gpustack_url --token your_gpustack_token
```

!!! note

    1. **支持异构集群。** 无论设备类型如何，只需指定 `--server-url` 和 `--token` 参数即可将其作为工作节点加入当前 GPUStack。

    2. 可通过在 docker run 命令后追加参数为 `gpustack start` 命令设置额外标志。详情请参阅 [CLI 参考](../../cli-reference/start.md)。

## pip 安装

### 前置条件

- Python 3.10 ~ 3.12

检查 Python 版本：

```bash
python -V
```

### 安装 GPUStack

1. 在有网络的环境中下载所需的包和工具：

```bash
pip download "gpustack[audio]" -d gpustack-packages
```

如无需音频模型支持，可直接运行：

```bash
pip download gpustack -d gpustack-packages
```

2. 将 `gpustack-packages` 目录传输到离线环境。

3. 在离线环境中安装 GPUStack：

```bash
pip install --no-index --find-links gpustack-packages "gpustack[audio]"
```

如无需音频模型支持，可直接运行：

```bash
pip install --no-index --find-links gpustack-packages gpustack
```

验证安装：

```bash
gpustack version
```

### 运行 GPUStack

运行以下命令以启动 GPUStack 服务器及内置工作节点：

```bash
gpustack start
```

如需更改默认服务器端口 80，请使用 `--port` 参数：

```bash
gpustack start --port 9090
```

如有端口冲突或需自定义启动参数，请参阅 [CLI 参考](../../cli-reference/start.md)。

检查启动日志是否正常：

```bash
tail -200f ~/.gpustack/log/gpustack.log
```

若日志正常，可在浏览器中打开 `http://your_host_ip` 访问 GPUStack UI。使用用户名 `admin` 和默认密码登录。可通过以下命令获取默认密码：

```bash
cat ~/.gpustack/initial_admin_password
```

### （可选）添加工作节点

你可以为 GPUStack 添加更多 Ascend GPU 节点。需在其他 Ascend GPU 节点上添加工作节点，并指定 `--server-url` 和 `--token` 参数加入 GPUStack。

在 GPUStack **服务器节点**上运行以下命令获取 token：

```bash
cat ~/.gpustack/token
```

在工作节点上运行以下命令注册到 GPUStack 服务器（请替换 URL 和 token）：

```bash
gpustack start --server-url http://your_gpustack_url --token your_gpustack_token
```

!!! note

    1. **支持异构集群。** 无论设备类型如何，只需指定 `--server-url` 和 `--token` 参数即可将其作为工作节点加入当前 GPUStack。

    2. 可通过在 `gpustack start` 命令后追加参数为 `gpustack start` 命令设置额外标志。详情请参阅 [CLI 参考](../../cli-reference/start.md)。 