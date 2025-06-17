# OpenAI 兼容 API

aiMindServe 通过 `/v1-openai` 路径提供 [OpenAI 兼容的 API](https://platform.openai.com/docs/api-reference)。除了 `models` 端点（该端点保留用于 aiMindServe 管理 API）外，大多数 API 也可以在 `/v1` 路径下作为别名使用。

## 支持的端点

以下 API 端点受到支持：

- [x] [列出模型](https://platform.openai.com/docs/api-reference/models/list)
- [x] [创建补全](https://platform.openai.com/docs/api-reference/completions/create)
- [x] [创建聊天补全](https://platform.openai.com/docs/api-reference/chat/create)
- [x] [创建嵌入](https://platform.openai.com/docs/api-reference/embeddings/create)
- [x] [创建图像](https://platform.openai.com/docs/api-reference/images/create)
- [x] [创建图像编辑](https://platform.openai.com/docs/api-reference/images/createEdit)
- [x] [创建语音](https://platform.openai.com/docs/api-reference/audio/createSpeech)
- [x] [创建转录](https://platform.openai.com/docs/api-reference/audio/createTranscription)

## 使用方法

以下是使用不同语言调用 API 的示例：

### curl

```bash
export GPUSTACK_API_KEY=your_api_key
curl http://your_aimindserve_server_url/v1-openai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GPUSTACK_API_KEY" \
  -d '{
    "model": "llama3",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "stream": true
  }'
```

### OpenAI Python API 库

```python
from openai import OpenAI

client = OpenAI(base_url="http://your_gpustack_server_url/v1", api_key="your_api_key")

completion = client.chat.completions.create(
  model="llama3",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
```

### OpenAI Node API 库

```javascript
const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: "your_api_key",
  baseURL: "http://your_gpustack_server_url/v1",
});

async function main() {
  const params = {
    model: "llama3",
    messages: [
      {
        role: "system",
        content: "You are a helpful assistant.",
      },
      {
        role: "user",
        content: "Hello!",
      },
    ],
  };
  const chatCompletion = await openai.chat.completions.create(params);
  console.log(chatCompletion.choices[0].message);
}
main();
``` 