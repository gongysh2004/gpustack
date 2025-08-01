# 推理后端

aiMindServe 支持以下推理后端：

- [llama-box](#llama-box)
- [vLLM](#vllm)
- [vox-box](#vox-box)
- [Ascend MindIE](#ascend-mindie-实验性)

当用户部署模型时，后端会根据以下标准自动选择：

- 如果模型是 [GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) 模型，则使用 `llama-box`。
- 如果模型是已知的 `文本转语音` 或 `语音转文本` 模型，则使用 `vox-box`。
- 否则，使用 `vLLM`。

## llama-box

[llama-box](https://github.com/gpustack/llama-box) 是一个基于 [llama.cpp](https://github.com/ggml-org/llama.cpp) 和 [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) 的 LM 推理服务器。

### 支持的平台

llama-box 后端支持 Linux、macOS 和 Windows（在 Windows ARM 架构上仅支持 CPU 卸载）平台。

### 支持的模型

- LLMs：有关支持的 LLM，请参阅 llama.cpp [README](https://github.com/ggml-org/llama.cpp#description)。
- 扩散模型：支持的模型列在此 [Hugging Face 集合](https://huggingface.co/collections/gpustack/image-672dafeb2fa0d02dbe2539a9) 或此 [ModelScope 集合](https://modelscope.cn/collections/Image-fab3d241f8a641) 中。
- 重排序模型：支持的模型可以在此 [Hugging Face 集合](https://huggingface.co/collections/gpustack/reranker-6721a234527f6fcd90deedc4) 或此 [ModelScope 集合](https://modelscope.cn/collections/Reranker-7576210e79de4a) 中找到。

### 支持的功能

#### 允许 CPU 卸载

启用 CPU 卸载后，aiMindServe 会优先将尽可能多的层加载到 GPU 上以优化性能。如果 GPU 资源有限，一些层将被卸载到 CPU，只有在没有 GPU 可用时才使用完整的 CPU 推理。

#### 允许跨工作节点分布式推理

启用跨多个工作节点的分布式推理。主模型实例将与一个或多个其他工作节点上的后端实例通信，将计算任务卸载给它们。

#### 多模态语言模型

Llama-box 支持以下视觉语言模型。使用视觉语言模型时，聊天补全 API 支持图像输入。

- LLaVA 系列
- MiniCPM VL 系列
- Qwen2 VL 系列
- GLM-Edge-V 系列
- Granite VL 系列
- Gemma3 VL 系列
- SmolVLM 系列
- Pixtral 系列
- MobileVLM 系列
- Mistral Small 3.1
- Qwen2.5 VL 系列

!!! 注意

    部署视觉语言模型时，aiMindServe 默认下载并使用模式为 `*mmproj*.gguf` 的多模态投影文件。如果有多个文件匹配该模式，aiMindServe 会选择精度更高的文件（例如，`f32` 优于 `f16`）。如果默认模式不匹配投影文件或您想使用特定的文件，您可以通过在模型配置中设置 `--mmproj` 参数来自定义多模态投影文件。您可以指定模型源中投影文件的相对路径。这种语法是一种简写，aiMindServe 将从源下载文件并在使用时规范化路径。

### 参数参考

有关 llama-box 支持的参数的完整列表，请参阅[此处](https://github.com/gpustack/llama-box#usage)。

## vLLM

[vLLM](https://github.com/vllm-project/vllm) 是一个高吞吐量和内存效率高的 LLM 推理引擎。它是生产环境中运行 LLM 的热门选择。vLLM 无缝支持大多数最先进的开源模型，包括：类 Transformer 的 LLM（例如，Llama）、专家混合 LLM（例如，Mixtral）、嵌入模型（例如，E5-Mistral）、多模态 LLM（例如，LLaVA）

默认情况下，aiMindServe 根据模型的元数据估算模型实例的 VRAM 需求。您可以自定义参数以满足您的需求。以下 vLLM 参数可能有用：

- `--gpu-memory-utilization`（默认值：0.9）：用于模型实例的 GPU 内存比例。
- `--max-model-len`：模型上下文长度。对于大上下文模型，aiMindServe 自动将此参数设置为 `8192` 以简化模型部署，特别是在资源受限的环境中。您可以自定义此参数以满足您的需求。
- `--tensor-parallel-size`：张量并行副本数。默认情况下，aiMindServe 根据可用的 GPU 资源和模型的内存需求估算来设置此参数。您可以自定义此参数以满足您的需求。

有关更多详细信息，请参阅 [vLLM 文档](https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#command-line-arguments-for-the-server)。

### 支持的平台

vLLM 后端在 AMD64 Linux 上运行。

!!! 注意

    1. 当用户使用安装脚本在 amd64 Linux 上安装 aiMindServe 时，vLLM 会自动安装。
    2. 当用户使用 vLLM 后端部署模型时，aiMindServe 默认将工作节点标签选择器设置为 `{"os": "linux", "arch": "amd64"}`，以确保模型实例被调度到适当的工作节点。您可以在模型配置中自定义工作节点标签选择器。

### 支持的模型

有关支持的模型，请参阅 vLLM [文档](https://docs.vllm.ai/en/stable/models/supported_models.html)。

### 支持的功能

#### 多模态语言模型

vLLM 支持[此处](https://docs.vllm.ai/en/stable/models/supported_models.html#multimodal-language-models)列出的多模态语言模型。当用户使用 vLLM 后端部署视觉语言模型时，聊天补全 API 支持图像输入。

#### 跨工作节点分布式推理（实验性）

vLLM 支持使用 [Ray](https://ray.io) 跨多个工作节点进行分布式推理。您可以通过使用 `--enable-ray` 启动参数在 aiMindServe 中启用 Ray 集群，允许 vLLM 跨多个工作节点运行分布式推理。

!!! 警告 "已知限制"

    1. aiMindServe 服务器和所有参与的工作节点必须在 Linux 上运行并使用相同版本的 Python，这是 Ray 的要求。
    2. 模型文件必须在所有参与的工作节点上的相同路径可访问。您必须使用共享文件系统或将模型文件下载到所有参与的工作节点上的相同路径。
    3. 每个工作节点一次只能分配给一个分布式 vLLM 模型实例。
    4. 如果自定义 vLLM 版本的 Ray 分布式执行器实现与内置 vLLM 版本不兼容，则可能无法工作。
    5. 如果您使用 Docker 安装 aiMindServe，必须使用主机网络模式以利用 RDMA/InfiniBand 并确保节点之间的连接。

在以下条件下支持自动调度：

- 参与的工作节点具有相同数量的 GPU。
- 工作节点中的所有 GPU 满足 gpu_memory_utilization（默认为 0.9）要求。
- GPU 总数可以被注意力头数整除。
- 总 VRAM 声明大于估算的 VRAM 声明。

如果不满足上述条件，模型实例将不会自动调度。但是，您可以通过在模型配置中选择所需的工作节点/GPU 来手动调度它。

### 参数参考

有关 vLLM 支持的参数的完整列表，请参阅[此处](https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#command-line-arguments-for-the-server)。

## vox-box

[vox-box](https://github.com/gpustack/vox-box) 是一个专为部署文本转语音和语音转文本模型设计的推理引擎。它还提供了一个与 OpenAI 音频 API 完全兼容的 API。

### 支持的平台

vox-box 后端支持 Linux、macOS 和 Windows 平台。

!!! 注意

    1. 要使用 NVIDIA GPU，确保工作节点上安装了以下 NVIDIA 库：
        - [cuBLAS for CUDA 12](https://developer.nvidia.com/cublas)
        - [cuDNN 9 for CUDA 12](https://developer.nvidia.com/cudnn)
    2. 当用户使用安装脚本在 Linux、macOS 和 Windows 上安装 aiMindServe 时，vox-box 会自动安装。
    3. CosyVoice 模型在 Linux AMD 架构和 macOS 上原生支持。但是，这些模型在 Linux ARM 或 Windows 架构上不受支持。

### 支持的模型

| 模型 | 类型 | 链接 | 支持的平台 |
| ------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Faster-whisper-large-v3 | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v3), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-large-v3) | Linux, macOS, Windows |
| Faster-whisper-large-v2 | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v2), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-large-v2) | Linux, macOS, Windows |
| Faster-whisper-large-v1 | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v1), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-large-v1) | Linux, macOS, Windows |
| Faster-whisper-medium | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-medium), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-medium) | Linux, macOS, Windows |
| Faster-whisper-medium.en | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-medium.en), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-medium.en) | Linux, macOS, Windows |
| Faster-whisper-small | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-small), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-small) | Linux, macOS, Windows |
| Faster-whisper-small.en | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-small.en), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-small.en) | Linux, macOS, Windows |
| Faster-distil-whisper-large-v3 | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-distil-whisper-large-v3), [ModelScope](https://modelscope.cn/models/gpustack/faster-distil-whisper-large-v3) | Linux, macOS, Windows |
| Faster-distil-whisper-large-v2 | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-distil-whisper-large-v2), [ModelScope](https://modelscope.cn/models/gpustack/faster-distil-whisper-large-v2) | Linux, macOS, Windows |
| Faster-distil-whisper-medium.en | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-distil-whisper-medium.en), [ModelScope](https://modelscope.cn/models/gpustack/faster-distil-whisper-medium.en) | Linux, macOS, Windows |
| Faster-whisper-tiny | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-tiny), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-tiny) | Linux, macOS, Windows |
| Faster-whisper-tiny.en | 语音转文本 | [Hugging Face](https://huggingface.co/Systran/faster-whisper-tiny.en), [ModelScope](https://modelscope.cn/models/gpustack/faster-whisper-tiny.en) | Linux, macOS, Windows |
| CosyVoice-300M-Instruct | 文本转语音 | [Hugging Face](https://huggingface.co/FunAudioLLM/CosyVoice-300M-Instruct), [ModelScope](https://modelscope.cn/models/gpustack/CosyVoice-300M-Instruct) | Linux(不支持 ARM), macOS, Windows(不支持) |
| CosyVoice-300M-SFT | 文本转语音 | [Hugging Face](https://huggingface.co/FunAudioLLM/CosyVoice-300M-SFT), [ModelScope](https://modelscope.cn/models/iic/CosyVoice-300M-SFT) | Linux(不支持 ARM), macOS, Windows(不支持) |
| CosyVoice-300M | 文本转语音 | [Hugging Face](https://huggingface.co/FunAudioLLM/CosyVoice-300M), [ModelScope](https://modelscope.cn/models/gpustack/CosyVoice-300M) | Linux(不支持 ARM), macOS, Windows(不支持) |
| CosyVoice-300M-25Hz | 文本转语音 | [ModelScope](https://modelscope.cn/models/iic/CosyVoice-300M-25Hz) | Linux(不支持 ARM), macOS, Windows(不支持) |
| CosyVoice2-0.5B | 文本转语音 | [Hugging Face](https://huggingface.co/FunAudioLLM/CosyVoice2-0.5B), [ModelScope](https://modelscope.cn/models/iic/CosyVoice2-0.5B) | Linux(不支持 ARM), macOS, Windows(不支持) |
| Dia-1.6B | 文本转语音 | [Hugging Face](https://huggingface.co/nari-labs/Dia-1.6B), [ModelScope](https://modelscope.cn/models/nari-labs/Dia-1.6B) | Linux(不支持 ARM), macOS, Windows(不支持) |

### 支持的功能

#### 允许 GPU/CPU 卸载

vox-box 支持将模型部署到 NVIDIA GPU。如果 GPU 资源不足，它将自动将模型部署到 CPU。

## Ascend MindIE（实验性）

[Ascend MindIE](https://www.hiascend.com/en/software/mindie) 是 [Ascend 硬件](https://www.hiascend.com/en/hardware/product) 上的高性能推理服务。

### 支持的平台

Ascend MindIE 后端仅在 Linux 平台上运行，包括 ARM64 和 x86_64 架构。

### 支持的模型

Ascend MindIE 支持[此处](https://www.hiascend.com/document/detail/zh/mindie/20RC1/modellist/mindie_modellist_0001.html)列出的各种模型。

在 aiMindServe 中，支持[大语言模型（LLM）](https://www.hiascend.com/document/detail/zh/mindie/20RC1/modellist/mindie_modellist_0001.html)和[多模态语言模型（VLM）](https://www.hiascend.com/document/detail/zh/mindie/20RC1/modellist/mindie_modellist_0002.html)。但是，目前还不支持_嵌入模型_和_多模态生成模型_。

### 支持的功能

Ascend MindIE 拥有[此处](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0001.html)概述的各种功能。

目前，aiMindServe 支持这些功能的一个子集，包括[量化](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0288.html)、[扩展上下文大小](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0295.html)、[专家混合（MoE）](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0297.html)、[前缀缓存](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0302.html)、[函数调用](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0303.html)、[多模态理解](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0304.html)、[多头潜在注意力（MLA）](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0305.html)。

!!! 注意

    1. 量化需要特定的权重，并且必须调整模型的 `config.json`，请按照[参考（指南）](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0288.html)准备正确的权重。
    2. 对于多模态理解功能，某些版本的 Ascend MindIE 的 API 与 OpenAI 不兼容，请关注此[问题](https://github.com/gpustack/gpustack/issues/1803)以获取更多支持。
    3. 某些功能是互斥的，因此在使用时要小心。

### 参数参考

Ascend MindIE 有可配置的[参数](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0004.html)和[环境变量](https://www.hiascend.com/document/detail/zh/mindie/20RC1/mindiellm/llmdev/mindie_llm0416.html)。

为了避免直接配置 JSON，aiMindServe 提供了一组命令行参数，如下所示。

| 参数 | 默认值 | 描述 |
| -------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `--trust-remote-code` | | 信任远程代码（用于模型加载）。 |
| `--npu-memory-fraction` | 0.9 | 用于模型执行器的 NPU 内存比例（0 到 1）。例如：`0.5` 表示 50% 的内存利用率。 |
| `--max-link-num` | 1000 | 最大并行请求数。 |
| `--token-timeout` | 60 | 令牌生成的超时时间（秒）。 |
| `--e2e-timeout` | 60 | E2E（从请求接受到推理停止）超时时间（秒）。 |
| `--max-seq-len` | 8192 | 模型上下文长度。如果未指定，将从模型配置中派生。 |
| `--max-input-token-len` | | 最大输入令牌长度。如果未指定，将从 `--max-seq-len` 派生。 |
| `--truncation` | | 当输入令牌长度超过 `--max-input-token-len` 和 `--max-seq-len` - 1 的最小值时截断。 |
| `--cpu-mem-size` | 5 | CPU 交换空间大小（GiB）。如果未指定，将使用默认值。 |
| `--cache-block-size` | 128 | KV 缓存块大小。必须是 2 的幂。 |
| `--max-batch-size` | 200 | 解码阶段批处理的最大请求数。 |
| `--max-prefill-batch-size` | 50 | 预填充阶段批处理的最大请求数。必须小于 `--max-batch-size`。 |
| `--max-preempt-count` | 0 | 解码期间允许的最大抢占请求数。必须小于 `--max-batch-size`。 |
| `--max-queue-delay-microseconds` | 5000 | 最大队列等待时间（微秒）。 |
| `--prefill-time-ms-per-req` | 150 | 每个请求的估计预填充时间（毫秒）。用于在预填充和解码阶段之间做出决定。 |
| `--prefill-policy-type` | 0 | 预填充阶段策略：<br> `0`：FCFS（先来先服务）。<br> `1`：STATE（与 FCFS 相同）。<br> `2`：PRIORITY（优先级队列）。<br> `3`：MLFQ（多级反馈队列）。 |
| `--decode-time-ms-per-req` | 50 | 每个请求的估计解码时间（毫秒）。与 `--prefill-time-ms-per-req` 一起用于批处理选择。 |
| `--decode-policy-type` | 0 | 解码阶段策略：<br> `0`：FCFS <br> `1`：STATE（优先处理被抢占或交换的请求）<br> `2`：PRIORITY <br> `3`：MLFQ |
| `--support-select-batch` | | 启用批处理选择。根据 `--prefill-time-ms-per-req` 和 `--decode-time-ms-per-req` 确定执行优先级。 |
| `--enable-prefix-caching` | | 启用前缀缓存。使用 `--no-enable-prefix-caching` 显式禁用。 |
| `--enforce-eager` | | 以急切模式发出操作符。 |
| `--dtype` | auto | 模型权重和激活的数据类型。<br> `auto`：使用模型配置的默认数据类型。<br> `half`/`float16`：用于 FP16。<br> `bfloat16`：用于 BF16。<br> `float`/`float32`：用于 FP32。 |
| `--rope-scaling` | | RoPE 缩放配置（JSON 格式）。例如：`{"type":"yarn","factor":4.0,"original_max_position_embeddings":32768}`。这将合并到模型结构的 `config.json` 中。 |
| `--rope-theta` | | RoPE theta 配置。这将合并到模型结构的 `config.json` 中。 |
| `--override-generation-config` | | 以 JSON 格式覆盖或设置生成配置。例如：`{"temperature": 0.5}`。这将合并到模型结构的 `generation_config.json` 中。 |
| `--metrics` | | 在 `/metrics` 端点公开指标。 |
| `--log-level` | Info | MindIE 的日志级别。选项：`Verbose`、`Info`、`Warning`、`Warn`、`Error`、`Debug`。 |

!!! 注意

    aiMindServe 允许用户在模型部署期间注入自定义环境变量，但是，某些变量可能与 aiMindServe 管理冲突。因此，aiMindServe 将覆盖/阻止这些变量。请将模型实例日志的输出与您的期望进行比较。 