# 使用视觉语言模型

**视觉语言模型（Vision Language Models）**能够同时处理视觉（图像）和语言（文本）数据，广泛应用于图像描述、视觉问答等多种场景。本指南将介绍如何在 aiMindServe 中部署和使用视觉语言模型（VLMs）。

这些模型的部署和使用流程基本一致，主要区别在于部署时需要设置的参数。更多参数说明请参考[后端参数](../user-guide/inference-backends.md#parameters-reference_1)。

本指南将涵盖以下模型的部署：

- **Llama3.2-Vision**
- **Qwen2-VL**
- **Pixtral**
- **Phi3.5-Vision**


## 步骤 1：部署视觉语言模型

### 从 Catalog 部署

Catalog 中的视觉语言模型带有 `vision` 能力标签。只要你的 GPU 资源充足且后端兼容（如 vLLM 后端需 amd64 Linux worker），选择 Catalog 中的视觉语言模型默认配置即可。

![catalog-vlm](../assets/using-models/using-vision-language-models/catalog-vlm.png)

### llama-box 自定义部署示例

使用 llama-box 部署 GGUF 格式的 VLM 时，aiMindServe 会自动处理多模态投影文件，开箱即用。

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model` 按钮，在下拉菜单中选择 `Hugging Face`。
2. 勾选 `GGUF` 复选框以筛选 GGUF 格式的模型。
3. 搜索 `bartowski/Qwen2-VL-2B-Instruct-GGUF`。
4. 选择 GGUF `Q4_K_M` 量化格式。
5. 点击 `保存` 按钮部署模型。

![部署 GGUF 模型](../assets/using-models/using-vision-language-models/deploy-model-gguf.png)

### vLLM 自定义部署示例

#### 部署 Llama3.2-Vision

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model` 按钮，选择 `Hugging Face`。
2. 搜索 `meta-llama/Llama-3.2-11B-Vision-Instruct`。
3. 展开配置中的 `Advanced` 区域，滚动到 `Backend Parameters`。
4. 多次点击 `Add Parameter` 按钮，添加以下参数：

- `--enforce-eager`
- `--max-num-seqs=16`
- `--max-model-len=8192`

5. 点击 `保存` 按钮。

![llama3.2-vl](../assets/using-models/using-vision-language-models/llama3.2-vl.png)

#### 部署 Qwen2-VL

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model` 按钮，选择 `Hugging Face`。
2. 搜索 `Qwen/Qwen2-VL-7B-Instruct`。
3. 点击 `保存` 按钮，默认配置即可。

#### 部署 Pixtral

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model` 按钮，选择 `Hugging Face`。
2. 搜索 `mistralai/Pixtral-12B-2409`。
3. 展开配置中的 `Advanced` 区域，滚动到 `Backend Parameters`。
4. 多次点击 `Add Parameter` 按钮，添加以下参数：

- `--tokenizer-mode=mistral`
- `--limit-mm-per-prompt=image=4`

5. 点击 `保存` 按钮。

#### 部署 Phi3.5-Vision

1. 在 aiMindServe UI 的 `Models` 页面点击 `Deploy Model` 按钮，选择 `Hugging Face`。
2. 搜索 `microsoft/Phi-3.5-vision-instruct`。
3. 展开配置中的 `Advanced` 区域，滚动到 `Backend Parameters`。
4. 点击 `Add Parameter` 按钮，添加以下参数：

- `--trust-remote-code`

5. 点击 `保存` 按钮。

## 步骤 2：与视觉语言模型交互

1. 在 aiMindServe UI 的 `试验场-》对话` 页面。
2. 在右上角下拉框中选择已部署的模型。
3. 点击输入框上方的 `上传图片` 按钮，上传图片。
4. 在输入框中输入提示词，例如"描述这张图片"。
5. 点击 `Submit` 按钮生成输出。

![playground-vl](../assets/using-models/using-vision-language-models/playground-vl.png) 