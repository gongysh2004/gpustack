# 与 RAGFlow 集成

RAGFlow 可以与 aiMindServe 集成，以利用本地部署的 LLM、嵌入、重排序、语音转文本和文本转语音功能。

## 部署模型

1. 在 aiMindServe UI 中，导航到 `Models` 页面，点击 `Deploy Model` 来部署你需要的模型。以下是一些示例模型：

- qwen3-8b
- qwen2.5-vl-3b-instruct
- bge-m3
- bge-reranker-v2-m3

![aimindserve-models](../assets/integrations/integration-aimindserve-models.png)

2. 在模型的操作中，打开 `API Access Info` 查看如何与该模型集成。

![aimindserve-api-access-info](../assets/integrations/integration-aimindserve-api-access-info.png)

## 创建 API 密钥

1. 导航到 `API Keys` 页面，点击 `New API Key`。

2. 填写名称，然后点击 `Save`。

3. 复制 API 密钥并保存以供后续使用。

## 将 aiMindServe 集成到 RAGFlow

1. 访问 RAGFlow UI，点击右上角的头像，选择 `Model Providers > GPUStack`，然后选择 `Add the model` 并填写：

- Model type：根据模型选择模型类型。

- Model name：名称必须与 aiMindServe 上部署的模型名称匹配。

- Base URL：`http://your-aimindserve-url`，URL 不应包含路径，且不要使用 `localhost`，因为它指的是容器内部网络。如果使用自定义端口，请确保包含它。同时，确保 URL 可以从 RAGFlow 容器内部访问（你可以使用 `curl` 测试）。

- API-Key：输入你从之前步骤复制的 API 密钥。

- Max Tokens：输入当前模型配置支持的最大 token 数。

点击 `OK` 添加模型：

![ragflow-add-model](../assets/integrations/integration-ragflow-add-model.png)

2. 根据需要添加其他模型，然后在 `Set default models` 中选择添加的模型并保存：

![ragflow-set-default-models](../assets/integrations/integration-ragflow-set-default-models.png)

现在你可以在 `Chat` 和 `Knowledge Base` 中使用这些模型，这里是一个简单的案例：

1. 进入 `Knowledge base` 创建新的知识库并添加你的文件：

![ragflow-create-knowledge-base](../assets/integrations/integration-ragflow-create-knowledge-base.png)

2. 导航到 `Retrieval testing` 并将重排序模型设置为 `bge-reranker-v2-m3`：

![ragflow-set-rerank-model](../assets/integrations/integration-ragflow-set-rerank-model.png)

3. 在 `Chat` 中，创建一个助手，链接之前创建的知识库，并选择聊天模型：

![ragflow-create-assistant](../assets/integrations/integration-ragflow-create-assistant.png)

4. 创建聊天会话 — 现在你可以与模型交互并查询知识库：

![ragflow-chat-with-model](../assets/integrations/integration-ragflow-chat-with-model.png)

5. 编辑助手并将模型切换到 `qwen2.5-vl-3b-instruct`。保存后，创建新的聊天并上传图片以启用多模态输入：

![ragflow-chat-with-vlm](../assets/integrations/integration-ragflow-chat-with-vlm.png) 