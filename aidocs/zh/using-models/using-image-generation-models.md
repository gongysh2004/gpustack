# 使用图像生成模型

aiMindServe 支持部署和运行最先进的**图像生成模型**。这些模型可以根据文本描述生成精美图片，广泛应用于设计、内容创作等领域。

本指南将带你了解如何在 aiMindServe 中部署和使用图像生成模型。

## 前置条件

在开始之前，请确保你具备以下条件：

- 至少 12GB 显存的 GPU。
- 可访问 Hugging Face 以下载模型文件。
- 已安装并运行 aiMindServe。如未安装，请参考[快速开始指南](../quickstart.md)。

## 步骤 1：部署 Stable Diffusion 模型

按照以下步骤从 Hugging Face 部署模型：

1. 在 aiMindServe UI 中进入 `Models` 页面。
2. 点击 `Deploy Model` 按钮。
3. 在下拉菜单中选择 `Hugging Face` 作为模型来源。
4. 在左上角搜索栏中输入模型名 `gpustack/stable-diffusion-v3-5-medium-GGUF`。
5. 在 `Available Files` 区域选择 `stable-diffusion-v3-5-medium-Q4_0.gguf` 文件。
6. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/using-image-generation-models/deploy-model.png)

部署后，你可以在 `Models` 页面监控模型状态。

![模型列表](../assets/using-models/using-image-generation-models/model-list.png)

## 步骤 2：使用模型生成图片

1. 在 aiMindServe UI 中进入 `Playground` > `Image` 页面。
2. 确认右上角 `Model` 下拉框中已选择已部署的模型。
3. 输入你想生成图片的文本描述。例如：

```
一位拥有长发、发丝如极光般缥缈的女性角色。背景以深蓝和紫色为主，营造神秘而戏剧性的氛围。角色面容安详，肤色苍白，五官立体。她身穿深色服饰，带有细腻花纹。整体画风偏幻想或超自然风格。
```

4. 在 `Sampler` 下拉框中选择 `euler`。
5. 将 `Sample Steps` 设置为 `20`。
6. 点击 `Submit` 按钮生成图片。

生成的图片会显示在界面中。由于生成过程涉及随机性，你的图片可能与示例略有不同。

![生成结果](../assets/using-models/using-image-generation-models/image-playground.png)

## 总结

通过上述设置，你可以根据文本提示生成独特且视觉效果出众的图片。欢迎尝试不同的提示词和参数，探索更多可能性。更多参数推荐请参考[图像生成模型推荐参数](./recommended-parameters-for-image-generation-models.md) 