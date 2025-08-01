# 重排序 API

在检索增强生成（RAG）场景中，重排序指的是在将检索到的文档或知识源展示给用户或用于答案生成前，选出最相关信息的过程。

aiMindServe 通过 `/v1/rerank` 路径提供 [Jina 兼容重排序 API](https://jina.ai/reranker/)。

## 支持的模型

当前可用于重排序的模型有：

- [bce-reranker-base_v1](https://huggingface.co/gpustack/bce-reranker-base_v1-GGUF)
- [jina-reranker-v1-turbo-en](https://huggingface.co/gpustack/jina-reranker-v1-turbo-en-GGUF)
- [jina-reranker-v1-tiny-en](https://huggingface.co/gpustack/jina-reranker-v1-tiny-en-GGUF)
- [bge-reranker-v2-m3](https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF)
- [gte-multilingual-reranker-base](https://huggingface.co/gpustack/gte-multilingual-reranker-base-GGUF) <span title="experimental">🧪</span>
- [jina-reranker-v2-base-multilingual](https://huggingface.co/gpustack/jina-reranker-v2-base-multilingual-GGUF) <span title="experimental">🧪</span>

## 使用方法

以下是调用重排序 API 的示例：

```bash
export GPUSTACK_API_KEY=your_api_key
curl http://your_aimindserve_server_url/v1/rerank \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GPUSTACK_API_KEY" \
    -d '{
        "model": "bge-reranker-v2-m3",
        "query": "What is a panda?",
        "top_n": 3,
        "documents": [
            "hi",
            "it is a bear",
            "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China."
        ]
    }' | jq
```

示例输出：

```json
{
  "model": "bge-reranker-v2-m3",
  "object": "list",
  "results": [
    {
      "document": {
        "text": "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China."
      },
      "index": 2,
      "relevance_score": 1.951932668685913
    },
    {
      "document": {
        "text": "it is a bear"
      },
      "index": 1,
      "relevance_score": -3.7347371578216553
    },
    {
      "document": {
        "text": "hi"
      },
      "index": 0,
      "relevance_score": -6.157620906829834
    }
  ],
  "usage": {
    "prompt_tokens": 69,
    "total_tokens": 69
  }
} 
```