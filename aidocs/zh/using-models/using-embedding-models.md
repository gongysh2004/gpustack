 # 使用嵌入模型

**文本嵌入（Text Embeddings）**是文本的数值化表示，能够捕捉语义信息，使机器能够理解不同文本之间的关系和相似性。它们本质上将文本转换为连续空间中的向量，语义相近的文本在空间中距离更近。文本嵌入广泛应用于自然语言处理、信息检索和推荐系统等场景。

本指南将演示如何在 aiMindServe 中部署嵌入模型，并使用已部署的模型生成文本嵌入。

## 前置条件

在开始之前，请确保你具备以下条件：

- 已安装并运行 aiMindServe。如未安装，请参考[快速开始指南](../quickstart.md)。
- 可访问 Hugging Face 以下载模型文件。

## 步骤 1：部署模型

按照以下步骤从 Hugging Face 部署模型：

1. 在 aiMindServe UI 中进入 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Hugging Face` 作为模型来源。
4. 勾选 `GGUF` 复选框以筛选 GGUF 格式的模型。
5. 在左上角搜索栏中输入模型名 `CompendiumLabs/bge-small-en-v1.5-gguf`。
6. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/using-embedding-models/deploy-model.png)

部署后，你可以在 `Models` 页面监控模型状态。

![模型列表](../assets/using-models/using-embedding-models/model-list.png)

## 步骤 2：生成 API 密钥

我们将通过 aiMindServe API 生成文本嵌入，因此需要一个 API 密钥：

1. 在 aiMindServe UI 中进入 `API Keys` 页面。
2. 点击 `New API Key` 按钮。
3. 输入 API 密钥名称并点击 `保存` 按钮。
4. 复制生成的 API 密钥。API 密钥只会显示一次，请妥善保存。

## 步骤 3：生成文本嵌入

模型部署并获取 API 密钥后，你可以通过 aiMindServe API 生成文本嵌入。以下是使用 `curl` 的示例脚本：

```bash
export SERVER_URL=<your-server-url>
export GPUSTACK_API_KEY=<your-api-key>
curl $SERVER_URL/v1-openai/embeddings \
  -H "Authorization: Bearer $GPUSTACK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "The food was delicious and the waiter...",
    "model": "bge-small-en-v1.5",
    "encoding_format": "float"
  }'
```

将 `<your-server-url>` 替换为你的 aiMindServe 服务器地址，`<your-api-key>` 替换为上一步生成的 API 密钥。

示例响应：

```json
{
  "data": [
    {
      "embedding": [
        -0.012189436703920364, 0.016934078186750412, 0.003965042531490326,
        -0.03453584015369415, -0.07623119652271271, -0.007116147316992283,
        0.11278388649225235, 0.019714849069714546, 0.010370955802500248,
        -0.04219457507133484, -0.029902394860982895, 0.01122555136680603,
        0.022912170737981796, 0.031186765059828758, 0.006303929258137941,
        # ... 其他数值
      ],
      "index": 0,
      "object": "embedding"
    }
  ],
  "model": "bge-small-en-v1.5",
  "object": "list",
  "usage": { "prompt_tokens": 12, "total_tokens": 12 }
}
```
