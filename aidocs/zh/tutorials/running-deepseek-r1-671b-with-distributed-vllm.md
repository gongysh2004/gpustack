# 使用分布式 vLLM 运行 DeepSeek R1 671B

本教程将指导您如何在 aiMindServe 集群上使用分布式 vLLM 配置并运行未量化的 **DeepSeek R1 671B**。由于该模型体积极大，通常需要跨多个工作节点进行分布式推理。

aiMindServe 使得使用 vLLM 进行分布式推理的设置和编排变得简单，能够以最少的手动配置运行像 DeepSeek R1 这样的大型模型。

## 前提条件

在开始之前，请确保满足以下要求：

- 您拥有足够数量的 Linux 节点，每个节点配备所需的 GPU。例如：

<div class="center-table" markdown>

| **GPU**          | **节点数量** |
| ---------------- | ------------ |
| H100/H800:8      | 2            |
| A100/A800-80GB:8 | 4            |
| A100/A800:8      | 8            |

</div>
- 推荐使用 NVLink 或 InfiniBand 等高速互连以获得最佳性能。
- 建议在每个节点上将模型文件下载到相同路径。虽然 aiMindServe 支持在线下载模型，但预先下载可节省时间，具体取决于网络速度。

!!! note

    - 本教程假设使用 4 个节点，每个节点配备 8 块 A800-80GB GPU，并通过 200G InfiniBand 互连。
    - A100/A800 GPU 不支持 DeepSeek R1 最初使用的 FP8 精度，因此我们使用 [Unsloth](https://huggingface.co/unsloth/DeepSeek-R1-BF16) 提供的 BF16 版本。

## 步骤 1：安装 aiMindServe Server

本教程使用 Docker 安装 aiMindServe，您也可以选择其他安装方式。

使用以下命令启动 aiMindServe 服务器：

```bash
docker run -d --name aimindserve-server \
    --restart=unless-stopped \
    --gpus all \
    --network=host \
    --ipc=host \
    -v aimindserve-data:/var/lib/gpustack \
    -v /path/to/your/model:/path/to/your/model \
    -e NCCL_SOCKET_IFNAME=eth2 \
    -e GLOO_SOCKET_IFNAME=eth2 \
    aimindserve/aimindserve --enable-ray --bootstrap-password=ailinks#QAZ
```

!!! note

    - 将 `/path/to/your/model` 替换为实际路径。
    - 设置 `NCCL_SOCKET_IFNAME` 和 `GLOO_SOCKET_IFNAME` 为用于节点间通信的网络接口。此处以 eth2 为例。
    - `--enable-ray` 参数用于启用 Ray 分布式推理，vLLM 需要此功能。

aiMindServe 服务器启动后，运行以下命令获取 worker 注册 token：

```bash
docker exec aimindserve-server cat /var/lib/gpustack/token
```

## 步骤 2：安装 aiMindServe Worker

在**每个工作节点**上，运行以下命令启动 aiMindServe worker：

```bash
docker run -d --name aimindserve-worker \
    --restart=unless-stopped \
    --gpus all \
    --network=host \
    --ipc=host \
    -v aimindserve-worker-data:/var/lib/gpustack \
    -v /path/to/your/model:/path/to/your/model \
    -e NCCL_SOCKET_IFNAME=eth2 \
    -e GLOO_SOCKET_IFNAME=eth2 \
    aimindserve/aimindserve \
    --server-url http://your_aimindserve_server_ip_or_hostname \
    --token your_aimindserve_token \
    --enable-ray
```

!!! note

    - 请根据实际情况替换路径、IP/主机名和 token。
    - 确保模型路径与服务器一致，并在所有 worker 节点上有效。

## 步骤 3：访问 aiMindServe UI

服务器和所有 worker 启动后，可通过浏览器访问 aiMindServe UI：

```
http://your_aimindserve_server_ip_or_hostname
```

使用 `admin` 用户名和密码登录。进入 `Resources` 页面，确认所有 worker 状态为 Ready，且 GPU 已列出。

![initial-resources](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/initial-resources.png)

## 步骤 4：部署 DeepSeek R1 模型

1. 进入 `Models` 页面。
2. 点击 `Deploy Model`。
3. 选择 `Local Path` 作为模型来源。
4. 在 `Name` 字段输入名称（如 `DeepSeek-R1`）。
5. 在 `Model Path` 中填写每个 worker 节点上 DeepSeek R1 模型文件所在目录。
6. 确保 `Backend` 选择为 `vLLM`。
7. 通过兼容性检查后，点击 `Save` 部署。

![deploy-model](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/deploy-model.png)

## 步骤 5：监控部署

您可以在 `Models` 页面监控部署状态。将鼠标悬停在 `distributed across workers` 上可查看 GPU 和 worker 使用情况。点击 `View Logs` 可实时查看模型加载进度日志。加载模型可能需要几分钟。

![model-info](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/model-info.png)

模型运行后，可回到 Resources 标签页查看 GPU 利用率。vLLM 默认使用 90% 的 GPU 显存，可在模型配置中调整。

![resources-loaded](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/resources-loaded.png)

## 步骤 6：通过 Playground 运行推理

模型部署并运行后，可通过 aiMindServe Playground 进行测试。

1. 进入 `Playground` -> `Chat`。
2. 若只部署了一个模型，将自动选中。否则可通过下拉菜单选择 `DeepSeek-R1`。
3. 输入提示词，与模型交互。

![playground-chat](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/playground-chat.png)

还可以使用 `Compare` 标签测试并发推理场景。

![playground-compare](../assets/tutorials/running-deepseek-r1-671b-with-distributed-vllm/playground-compare.png)

至此，您已成功在 aiMindServe 集群上使用分布式 vLLM 部署并运行 DeepSeek R1 671B。欢迎在您的应用中探索模型性能和能力。

如需进一步帮助，请联系 aiMindServe 支持团队。 