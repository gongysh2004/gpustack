# 使用大语言模型

**大语言模型（LLMs）**是能够理解和生成类人文本的强大 AI 模型，广泛应用于聊天机器人、内容生成、代码补全等场景。

本指南将介绍如何在 aiMindServe 中部署和使用大语言模型。

## 前置条件

在开始之前，请确保你具备以下条件：

- 一台配备一块或多块 GPU（总显存不少于 30GB）的 Linux 机器。我们将使用仅支持 Linux 的 vLLM 后端。
- 可访问 [Hugging Face](https://huggingface.co/) 或 [ModelScope](https://www.modelscope.cn/) 以下载模型文件。
- 已安装并运行 aiMindServe。如未安装，请参考[快速开始指南](../quickstart.md)。

## 步骤 1：部署大语言模型

### 从 Catalog 部署

Catalog 中的大语言模型带有 `LLM` 分类标签。只要你的 GPU 资源充足且后端兼容（如 vLLM 后端需 amd64 Linux worker），选择 Catalog 中的大语言模型默认配置即可。

以部署 `DeepSeek R1` 为例：

1. 在 aiMindServe UI 中进入 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Catalog` 作为模型来源。
4. 在 Catalog 列表页面左上角搜索栏输入 `DeepSeek`。
5. 查看模型描述、最大上下文长度和支持的参数规模。

![模型列表](../assets/using-models/using-large-language-models/model-list.png)

#### 使用 llama-box 部署

1. 在 Catalog 中选择 `Deepseek R1`。
2. 在 Size 选项中选择 `7B`。
3. 点击 `保存` 按钮部署模型。

![部署 GGUF 模型](../assets/using-models/using-large-language-models/deploy-model-llama-box.png)

部署后，你可以在 `Models` 页面监控模型状态，等待其启动。

#### 使用 vLLM 部署

1. 在 Catalog 中选择 `Deepseek R1`。
2. 由于模型名称即为访问 ID，不能与已创建的名称重复，请将默认模型名改为 `deepseek-r1-vllm`。
3. 选择 `vLLM` 后端。
4. 在 Size 选项中选择 `7B`。
5. 点击 `保存` 按钮部署模型。

![部署 Safetensors 模型](../assets/using-models/using-large-language-models/deploy-model-vllm.png)

部署后，你可以在 `Models` 页面监控模型状态，等待其启动。

## 步骤 2：使用大语言模型生成文本

1. 在 aiMindServe UI 中进入 `Playground` > `Chat` 页面。
2. 确认右上角 `Model` 下拉框中已选择已部署的模型。
3. 输入文本生成提示。例如：

```
2, 4, 6, 8, > 下一个数字是多少？
```

4. 可根据需要调整右侧参数。
5. 点击 `Submit` 按钮生成文本。

生成的推理过程和结果会显示在界面中。

![生成结果](../assets/using-models/using-large-language-models/generated.png)

通过以上步骤，你可以利用大语言模型在 aiMindServe 上进行 AI 文本生成和自然语言处理任务。欢迎尝试不同的提示词和参数，探索 LLM 的全部能力！ 