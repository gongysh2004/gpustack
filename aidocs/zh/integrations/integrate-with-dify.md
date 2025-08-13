# 与 Dify 集成

Dify 可以与 aiMindServe 集成，以利用本地部署的 LLM、嵌入、重排序、图像生成、语音转文本和文本转语音功能。

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

## 将 aiMindServe 集成到 Dify

1. 访问 Dify UI，点击右上角的 `PLUGINS`，选择 `Install from Marketplace`，搜索 GPUStack 插件并选择安装。

![dify-install-aimindserve-plugin](../assets/integrations/integration-dify-install-aimindserve-plugin.png)

2. 安装完成后，进入 `Settings > Model Provider > aiMindServe`，然后选择 `Add Model` 并填写：

- Model Type：根据模型选择模型类型。

- Model Name：名称必须与 aiMindServe 上部署的模型名称匹配。

- Server URL：`http://your-aimindserve-url`，不要使用 `localhost`，因为它指的是容器内部网络。如果使用自定义端口，请确保包含它。同时，确保 URL 可以从 Dify 容器内部访问（你可以使用 `curl` 测试）。

- API Key：输入你从之前步骤复制的 API 密钥。

点击 `Save` 添加模型：

![dify-add-model](../assets/integrations/integration-dify-add-model.png)

根据需要添加其他模型，然后在 `System Model Settings` 中选择添加的模型并保存：

![dify-system-model-settings](../assets/integrations/integration-dify-system-model-settings.png)

现在你可以在 `Studio` 和 `Knowledge` 中使用这些模型，这里是一个简单的案例：

1. 进入 `Knowledge` 创建知识库，并上传你的文档：

![dify-create-knowledge](../assets/integrations/integration-dify-create-knowledge.png)

2. 配置分块设置和检索设置。使用嵌入模型生成文档嵌入，使用重排序模型进行检索排序。

![dify-set-embedding-and-rerank-model](../assets/integrations/integration-dify-set-embedding-and-rerank-model.png)

3. 成功导入文档后，在 `Studio` 中创建一个应用，添加之前创建的知识库，选择聊天模型，并与之交互：

![dify-chat-with-model](../assets/integrations/integration-dify-chat-with-model.png)

4. 将模型切换到 `qwen2.5-vl-3b-instruct`，移除之前添加的知识库，启用 `Vision`，并在聊天中上传图片以激活多模态输入：

![dify-chat-with-vlm](../assets/integrations/integration-dify-chat-with-vlm.png) 