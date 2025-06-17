# OpenAI 兼容 API

aiMindServe 通过 `/v1-openai` 路径提供 [OpenAI 兼容的 API](https://platform.openai.com/docs/api-reference)。除了 `models` 端点（保留用于 aiMindServe 管理 API）外，大多数 API 也可以在 `/v1` 路径下作为别名使用。

对于所有支持 OpenAI 兼容 API 的应用程序和框架，你可以通过 aiMindServe 提供的 OpenAI 兼容 API 集成和使用部署在 aiMindServe 上的模型。

## 支持的端点

支持以下 API 端点：

- [x] [列出模型](https://platform.openai.com/docs/api-reference/models/list)
- [x] [创建补全](https://platform.openai.com/docs/api-reference/completions/create)
- [x] [创建聊天补全](https://platform.openai.com/docs/api-reference/chat/create)
- [x] [创建嵌入](https://platform.openai.com/docs/api-reference/embeddings/create)
- [x] [创建图像](https://platform.openai.com/docs/api-reference/images/create)
- [x] [创建图像编辑](https://platform.openai.com/docs/api-reference/images/createEdit)
- [x] [创建语音](https://platform.openai.com/docs/api-reference/audio/createSpeech)
- [x] [创建转录](https://platform.openai.com/docs/api-reference/audio/createTranscription)

## 重排序 API

在检索增强生成（RAG）的上下文中，重排序是指在将检索到的文档或知识源呈现给用户或用于生成答案之前，选择最相关信息的过程。

需要注意的是，OpenAI 兼容的 API 不提供 `rerank` API，因此 aiMindServe 通过 `/v1/rerank` 路径提供 [Jina 兼容的重排序 API](https://jina.ai/reranker/)。 