# 工具调用推理

工具调用（Tool Calling）允许您将模型连接到外部工具和系统。这对于赋能 AI 助手或在应用与模型之间构建深度集成非常有用。

本教程将指导您如何在 aiMindServe 中设置和使用工具调用，扩展 AI 的能力。

!!! note

    1. 工具调用在 [llama-box](../user-guide/inference-backends.md#llama-box) 和 [vLLM](../user-guide/inference-backends.md#vllm) 推理后端均支持。
    2. 工具调用本质上是通过提示工程实现的，需要模型在训练时内置相关模板，因此并非所有 LLM 都支持工具调用。

## 前提条件

在继续之前，请确保：

- 已安装并运行 aiMindServe。
- 有一台带 GPU 的 Linux worker 节点。本教程以 [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) 为例，该模型至少需要 18GB 显存。
- 可以访问 Hugging Face 下载模型文件。

## 步骤 1：部署模型

### 从目录部署

支持工具调用的 LLM 在目录中会标记 `tools` 能力。选择此类模型时，工具调用默认启用。

### llama-box 自定义部署示例

使用 llama-box 部署 GGUF 模型时，若模型支持工具调用，则默认启用。

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model`，下拉菜单选择 `Hugging Face`。
2. 启用 `GGUF` 复选框筛选 GGUF 格式模型。
3. 搜索 `Qwen/Qwen2.5-7B-Instruct-GGUF`。
4. 点击 `Save` 部署模型。

![Deploy GGUF Model](../assets/tutorials/inference-with-tool-calling/deploy-model-gguf.png)

### vLLM 自定义部署示例

使用 vLLM 部署模型时，需要在参数中手动启用工具调用。

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model`，下拉菜单选择 `Hugging Face`。
2. 搜索 `Qwen/Qwen2.5-7B-Instruct`。
3. 展开 `Advanced` 配置，滚动到 `Backend Parameters` 部分。
4. 点击 `Add Parameter`，添加如下参数：

- `--enable-auto-tool-choice`
- `--tool-call-parser=hermes`

5. 点击 `Save` 部署模型。

![Deploy Model](../assets/tutorials/inference-with-tool-calling/deploy-model.png)

部署完成后，可在 `Models` 页面监控模型状态。

## 步骤 2：生成 API Key

我们将通过 aiMindServe API 与模型交互。首先需要生成 API Key：

1. 在 aiMindServe UI 的 `API Keys` 页面点击 `New API Key`。
2. 输入名称并点击 `Save`。
3. 复制生成的 API Key 备用。

## 步骤 3：推理调用

模型部署并获得 API Key 后，可通过 aiMindServe API 调用模型。以下为 `curl` 示例（将 `<your-server-url>` 和 `<your-api-key>` 替换为实际值）：

```bash
export AIMINDSERVE_SERVER_URL=<your-server-url>
export AIMINDSERVE_API_KEY=<your-api-key>
curl $AIMINDSERVE_SERVER_URL/v1-openai/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
-d '{
  "model": "qwen2.5-7b-instruct",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Boston today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

示例响应：

```json
{
  "model": "qwen2.5-7b-instruct",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": [
          {
            "id": "chatcmpl-tool-b99d32848b324eaea4bac5a5830d00b8",
            "type": "function",
            "function": {
              "name": "get_current_weather",
              "arguments": "{\"location\": \"Boston, MA\", \"unit\": \"fahrenheit\"}"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ],
  "usage": {
    "prompt_tokens": 212,
    "total_tokens": 242,
    "completion_tokens": 30
  }
}
``` 