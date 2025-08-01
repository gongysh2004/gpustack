 # 使用音频模型

aiMindServe 支持运行语音转文本（Speech-to-Text）和文本转语音（Text-to-Speech）模型。语音转文本模型可将多种语言的音频输入转换为书面文本，而文本转语音模型则可将书面文本转换为自然且富有表现力的语音。

本指南将带你了解如何在 aiMindServe 中部署和使用语音转文本及文本转语音模型。

## 前置条件

在开始之前，请确保你具备以下条件：

- 采用 AMD64 架构的 Linux 系统或 macOS。
- 可访问 Hugging Face 以下载模型文件。
- 已安装并运行 aiMindServe。如未安装，请参考[快速开始指南](../quickstart.md)。

## 运行语音转文本模型

### 步骤 1：部署语音转文本模型

按照以下步骤从 Hugging Face 部署模型：

1. 在 aiMindServe UI 中进入 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Hugging Face` 作为模型来源。
4. 在左上角搜索栏中输入模型名 `Systran/faster-whisper-medium`。
5. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/using-audio-models/deploy-stt-model.png)

部署后，你可以在 `Models` 页面监控模型状态。

![模型列表](../assets/using-models/using-audio-models/stt-model-list.png)

### 步骤 2：与语音转文本模型交互

1. 在 aiMindServe UI 中进入 `Playground` > `Audio` 页面。
2. 选择 `Speech to Text` 标签页。
3. 在右上角下拉框中选择已部署的模型。
4. 点击 `上传` 按钮上传音频文件，或点击 `麦克风` 按钮录制音频。
5. 点击 `生成文本内容` 按钮生成文本。

![生成结果](../assets/using-models/using-audio-models/inference-stt-model.png)

## 运行文本转语音模型

### 步骤 1：部署文本转语音模型

按照以下步骤从 Hugging Face 部署模型：

1. 在 aiMindServe UI 中进入 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Hugging Face` 作为模型来源。
4. 在左上角搜索栏中输入模型名 `FunAudioLLM/CosyVoice-300M`。
5. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/using-audio-models/deploy-tts-model.png)

部署后，你可以在 `Models` 页面监控模型状态。

![模型列表](../assets/using-models/using-audio-models/tts-model-list.png)

### 步骤 2：与文本转语音模型交互

1. 在 aiMindServe UI 中进入 `Playground` > `Audio` 页面。
2. 选择 `Text to Speech` 标签页。
3. 在右上角下拉菜单中选择已部署的模型，并配置语音和输出音频格式。
4. 输入要生成的文本。
5. 点击 `提交` 按钮生成语音。

![生成结果](../assets/using-models/using-audio-models/inference-tts-model.png)
