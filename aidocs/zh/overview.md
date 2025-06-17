# 概述

![demo](../assets/gpustack-demo.gif)

aiMindServe 是一个开源的 AI 模型服务框架，旨在简化 AI 模型的部署和管理。它提供了一个统一的界面来部署和运行各种 AI 模型，包括大型语言模型（LLM）、图像生成模型、语音模型等。

aiMindServe 基于GPUStack 社区软件开发和封装，充分利用社区资源和生态。

## 主要特性

- **多模型支持**：支持多种 AI 模型，包括 LLM、图像生成、语音识别和合成等。
- **分布式部署**：支持在多个节点上分布式部署模型，实现负载均衡和资源优化。
- **统一 API**：提供统一的 API 接口，方便集成到现有系统中。
- **Web UI**：提供直观的 Web 界面，方便管理和监控模型。
- **容器化支持**：支持 Docker 部署，简化环境配置。
- **多平台支持**：支持 Linux、Windows 和 macOS。

## 支持的模型

aiMindServe 使用 [llama-box](https://github.com/gpustack/llama-box)（集成了 [llama.cpp](https://github.com/ggml-org/llama.cpp) 和 [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) 服务端）、[vLLM](https://github.com/vllm-project/vllm)、[昇腾 MindIE](https://www.hiascend.com/en/software/mindie) 和 [vox-box](https://github.com/gpustack/vox-box) 作为后端，支持多种模型。支持以下来源的模型：

- [Hugging Face](https://huggingface.co)
- [ModelScope](https://modelscope.cn)
- [Civitai](https://civitai.com)
- [OpenAI](https://openai.com)
- [Anthropic](https://anthropic.com)
- [Google](https://ai.google.dev)
- [Mistral AI](https://mistral.ai)
- [DeepSeek](https://deepseek.ai)
- [Qwen](https://qwenlm.github.io)
- [Yi](https://01.ai)
- [Gemma](https://ai.google.dev/gemma)
- [Phi](https://www.microsoft.com/en-us/research/project/phi-2/)
- [Orion](https://orionstar.ai)
- [Baichuan](https://www.baichuan-ai.com)
- [ChatGLM](https://chatglm.cn)
- [InternLM](https://internlm.ai)
- [XVERSE](https://xverse.cn)
- [Skywork](https://skywork.ai)
- [DeepSeek](https://deepseek.ai)


## 支持的模型类型

| 模型类型             | 支持的模型                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM**              | [Llama 3](https://huggingface.co/models?search=llama-3)、[Mistral](https://huggingface.co/models?search=mistral)、[Mixtral](https://huggingface.co/models?search=mixtral)、[DeepSeek](https://huggingface.co/models?search=deepseek)、[Yi](https://huggingface.co/models?search=yi)、[Gemma](https://huggingface.co/models?search=gemma)、[Phi](https://huggingface.co/models?search=phi)、[Orion](https://huggingface.co/models?search=orion)、[Baichuan](https://huggingface.co/models?search=baichuan)、[ChatGLM](https://huggingface.co/models?search=chatglm)、[InternLM](https://huggingface.co/models?search=internlm)、[XVERSE](https://huggingface.co/models?search=xverse)、[Skywork](https://huggingface.co/models?search=skywork) |
| **扩散模型**         | [Stable Diffusion](https://huggingface.co/models?search=gpustack/stable-diffusion)、[FLUX](https://huggingface.co/models?search=gpustack/flux)                                                                                                                                                                                                 |
| **嵌入模型**         | [BGE](https://huggingface.co/gpustack/bge-m3-GGUF)、[BCE](https://huggingface.co/gpustack/bce-embedding-base_v1-GGUF)、[Jina](https://huggingface.co/models?search=gpustack/jina-embeddings)                                                                                                                                                                                                 |
| **重排序模型**       | [BGE](https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF)、[BCE](https://huggingface.co/gpustack/bce-reranker-base_v1-GGUF)、[Jina](https://huggingface.co/models?search=gpustack/jina-reranker)                                                                                                                                                                                                 |
!!! note

    1. 由于技术变化比较快，模型支持列表会不断变化，最终的模型列表以售后服务提供为准。

## OpenAI 兼容 API

aiMindServe 提供 OpenAI 兼容的 API。有关详细信息，请参阅 [OpenAI 兼容 API](./user-guide/openai-compatible-apis.md)
