# 编辑图片

你可以使用图像模型通过选择要编辑的图像区域并描述期望的更改来**编辑图片**。模型会根据你的描述生成编辑后的图片。

本指南演示了如何在 aiMindServe 中编辑图片。

## 前置条件

在开始之前，请确保你具备以下条件：

- 至少 24GB 显存的 GPU。
- 可访问 Hugging Face 以下载模型文件。
- 已安装并运行 aiMindServe。如未安装，请参考[快速开始指南](../quickstart.md)。

本指南将使用 `FLUX.1-Fill-dev` 模型（`Q8_0` 量化）进行图片编辑。

## 步骤 1：部署模型

按照以下步骤从 Hugging Face 部署模型：

1. 在 aiMindServe UI 中进入 `Catalog` 页面。
2. 搜索并选择 `FLUX.1 Fill Dev` 模型。
3. 在弹窗中选择 `Q8_0` 量化。
4. 保持其他设置默认，点击 `保存` 按钮部署模型。

![部署模型](../assets/using-models/editing-images/image-edit-catalog.png)

部署后，你可以在 `Models` 页面监控模型状态。

## 步骤 2：使用模型编辑图片

1. 在 aiMindServe UI 中进入 `Playground` > `Image` 页面。
2. 点击顶部的 `Edit` 标签页。
3. 确认右上角 `Model` 下拉框中已选择已部署的模型。
4. 点击中间上传区域，上传[示例图片](../assets//using-models/editing-images/image-edit-example.png)。
5. 在示例图片的头发区域绘制遮罩。
6. 在 `Text Prompt` 输入框中输入以下文本提示：
   ```
   Pink short hair bang, natural
   ```
7. 点击 `Submit` 按钮生成编辑后的图片。

![图片编辑输入](../assets/using-models/editing-images/image-edit-input.png)

生成的图片会显示在界面中。由于生成过程涉及随机性，你的图片可能与示例略有不同。

![图片编辑输出](../assets/using-models/editing-images/image-edit-output.png)

如果你想复现上图结果，可以使用以下参数：

```
尺寸：768x1024(3:4)
采样方法：euler
调度方法：discrete
采样步数：50
引导：30.0
CFG Scale：1.0
Strength：1.0
种子：656821733471329
文本提示：Pink short hair bang, natural
```

## 步骤 3：使用图片编辑 API

点击 `View Code` 按钮，可查看如何通过 API 编程方式调用图片编辑功能的示例代码。

![查看代码](../assets/using-models/editing-images/view-code.png) 