 # 使用重排序模型

**重排序模型（Reranker Models）**是一类专门用于根据与查询的相关性提升项目列表排序的模型。它们常用于信息检索和搜索系统中，对初步检索结果进行优化，使更符合用户意图的内容排在前列。重排序模型会对初始文档列表进行重新排序，提升搜索引擎、推荐系统和问答等应用的精度。

本指南将演示如何在 aiMindServe 中部署和使用重排序模型。

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
5. 在左上角搜索栏中输入模型名 `gpustack/bge-reranker-v2-m3-GGUF`。
6. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/using-reranker-models/deploy-model.png)

部署后，你可以在 `Models` 页面监控模型状态。

![模型列表](../assets/using-models/using-reranker-models/model-list.png)

## 步骤 2：生成 API 密钥

我们将通过 aiMindServe API 与模型交互，因此需要一个 API 密钥：

1. 在 aiMindServe UI 中进入 `API Keys` 页面。
2. 点击 `New API Key` 按钮。
3. 输入 API 密钥名称并点击 `保存` 按钮。
4. 复制生成的 API 密钥。API 密钥只会显示一次，请妥善保存。

## 步骤 3：重排序

模型部署并获取 API 密钥后，你可以通过 aiMindServe API 对文档列表进行重排序。以下是使用 `curl` 的示例脚本：

```bash
export SERVER_URL=<your-server-url>
export AIMINDSERVE_API_KEY=<your-api-key>
curl $SERVER_URL/v1/rerank \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
    -d '{
        "model": "bge-reranker-v2-m3",
        "query": "什么是熊猫？",
        "top_n": 3,
        "documents": [
            "你好",
            "它是一种熊",
            "大熊猫（Ailuropoda melanoleuca），有时被称为熊猫或熊猫熊，是中国特有的熊科动物。"
        ]
    }' | jq
```

将 `<your-server-url>` 替换为你的 aiMindServe 服务器地址，`<your-api-key>` 替换为上一步生成的 API 密钥。

示例响应：

```json
{
  "model": "bge-reranker-v2-m3",
  "object": "list",
  "results": [
    {
      "document": {
        "text": "大熊猫（Ailuropoda melanoleuca），有时被称为熊猫或熊猫熊，是中国特有的熊科动物。"
      },
      "index": 2,
      "relevance_score": 1.951932668685913
    },
    {
      "document": {
        "text": "它是一种熊"
      },
      "index": 1,
      "relevance_score": -3.7347371578216553
    },
    {
      "document": {
        "text": "你好"
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
