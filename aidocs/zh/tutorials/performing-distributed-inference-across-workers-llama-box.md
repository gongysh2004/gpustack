# 跨工作节点执行分布式推理（llama-box）

本教程将指导您使用 aiMindServe 配置和运行跨多个工作节点的分布式推理。分布式推理允许您通过将计算工作负载分配到多个工作节点来处理更大的语言模型。当单个工作节点没有足够的资源（如显存）来独立运行整个模型时，这特别有用。

## 前提条件

在继续之前，请确保：

- 已安装并运行多节点 aiMindServe 集群。
- 可以访问 Hugging Face 以下载模型文件。

在本教程中，我们假设有一个包含两个节点的集群，每个节点都配备了一个 NVIDIA P40 GPU（22GB 显存），如下图所示：

![worker-list](../assets/tutorials/performing-distributed-inference-across-workers/worker-list.png)

我们的目标是运行一个需要比单个工作节点能提供的更多显存的大型语言模型。在本教程中，我们将使用 `Qwen/Qwen2.5-72B-Instruct` 模型，采用 `q2_k` 量化格式。可以使用 [gguf-parser](https://github.com/gpustack/gguf-parser-go) 工具估算运行此模型所需的资源：

```bash
gguf-parser --hf-repo Qwen/Qwen2.5-72B-Instruct-GGUF --hf-file qwen2.5-72b-instruct-q2_k-00001-of-00007.gguf --ctx-size=8192 --in-short --skip-architecture --skip-metadata --skip-tokenizer
```

```
+--------------------------------------------------------------------------------------+
| ESTIMATE                                                                             |
+----------------------------------------------+---------------------------------------+
|                      RAM                     |                 VRAM 0                |
+--------------------+------------+------------+----------------+----------+-----------+
| LAYERS (I + T + O) |     UMA    |   NONUMA   | LAYERS (T + O) |    UMA   |   NONUMA  |
+--------------------+------------+------------+----------------+----------+-----------+
|      1 + 0 + 0     | 259.89 MiB | 409.89 MiB |     80 + 1     | 2.50 GiB | 28.89 GiB |
+--------------------+------------+------------+----------------+----------+-----------+
```

从输出中可以看到，此模型的估计显存需求超过了每个工作节点上可用的 22GB 显存。因此，我们需要跨多个工作节点分配推理才能成功运行模型。

### 步骤 1：部署模型

按照以下步骤从 Hugging Face 部署模型，启用分布式推理：

1. 在 aiMindServe UI 中导航到 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Hugging Face` 作为模型来源。
4. 启用 `GGUF` 复选框以按 GGUF 格式筛选模型。
5. 使用左上角的搜索栏搜索模型名称 `Qwen/Qwen2.5-72B-Instruct-GGUF`。
6. 在 `Available Files` 部分，选择 `q2_k` 量化格式。
7. 展开 `Advanced` 部分并向下滚动。确认 `Allow Distributed Inference Across Workers` 选项已启用（默认启用）。aiMindServe 将评估集群中的可用资源，并在需要时以分布式方式运行模型。
8. 点击 `Save` 按钮部署模型。

![Deploy Model](../assets/tutorials/performing-distributed-inference-across-workers/deploy-model.png)

### 步骤 2：验证模型部署

模型部署完成后，在 `Models` 页面上验证部署，您可以查看模型如何在多个工作节点上运行的详细信息。

![model-list](../assets/tutorials/performing-distributed-inference-across-workers/model-list.png)

您还可以通过导航到 `Resources` 页面来检查工作节点和 GPU 资源使用情况。

![gpu-usage](../assets/tutorials/performing-distributed-inference-across-workers/gpu-usage.png)

最后，转到 `Playground` 页面与模型交互，验证一切是否正常运行。

![playground](../assets/tutorials/performing-distributed-inference-across-workers/playground.png) 