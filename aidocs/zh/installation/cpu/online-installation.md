# CPU上安装

在 aiMindServe 中，`llama-box` 和 `vox-box` 后端支持 CPU 推理。但与 GPU 相比，CPU 性能显著较低，因此仅推荐用于测试或小规模场景。

## 支持的设备

- [x] CPU（AMD64，需支持 AVX2 或 ARM64，需支持 NEON）

## 支持的平台

| 操作系统 | 架构           | 支持的安装方式                                                                                                                         |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Linux    | AMD64<br>ARM64 | [Docker 安装](#docker-安装)|

## 支持的后端

- [x] llama-box
- [x] vox-box

## 前置条件

- [端口要求](../installation-requirements.md#端口要求)
- CPU（AMD64，需支持 AVX2 或 ARM64，需支持 NEON）

=== "Linux"

    检查 CPU 是否支持：

    === "AMD64"

        ```bash
        lscpu | grep avx2
        ```

    === "ARM64"

        ```bash
        grep -E -i "neon|asimd" /proc/cpuinfo
        ```


## aiMindServe 安装

### 前置条件

- [Docker](https://docs.docker.com/engine/install/)

### 运行 aiMindServe

运行以下命令以启动 aiMindServe 服务器及内置工作节点（推荐 host 网络模式）：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-cpu
```

如需更改默认服务器端口 80，请使用 `--port` 参数：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-cpu \
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

你可以为 aiMindServe 添加更多 CPU 节点。需在其他 CPU 节点上添加工作节点，并指定 `--server-url` 和 `--token` 参数加入 aiMindServe

在 aiMindServe **服务器节点**上运行以下命令获取 token：

```bash
docker exec -it gpustack cat /var/lib/gpustack/token
```

在工作节点上运行以下命令注册到 aiMindServe 服务器（请替换 URL 和 token）：

```bash
docker run -d --name gpustack \
    --restart=unless-stopped \
    --network=host \
    -v gpustack-data:/var/lib/gpustack \
    gpustack/gpustack:latest-cpu \
    --server-url http://your_gpustack_url --token your_gpustack_token
```

!!! note

    1. **支持异构集群。** 无论设备类型如何，只需指定 `--server-url` 和 `--token` 参数即可将其作为工作节点加入当前 aiMindServe。

    2. 可通过在 docker run 命令后追加参数为 `gpustack start` 命令设置额外标志。详情请参阅 [CLI 参考](../../cli-reference/start.md)。

