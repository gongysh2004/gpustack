---
hide:
  - toc
---

# aiMindServe draw

使用扩散模型生成图像。

```bash
gpustack draw [model] [prompt]
```

## 位置参数

| 名称   | 描述                              |
| ------ | ---------------------------------------- |
| model  | 用于图像生成的模型。   |
| prompt | 用于图像生成的文本提示词。 |

`model` 可以是以下之一：

1. aiMindServe 模型的名称。在使用之前，您需要在 aiMindServe 中创建该模型。
2. 以 Ollama 风格引用的 Hugging Face GGUF 扩散模型。使用此选项时，如果模型尚未可用，将会部署该模型。未指定时默认使用 `Q4_0` 标签。示例：

   - `hf.co/gpustack/stable-diffusion-v3-5-large-turbo-GGUF`
   - `hf.co/gpustack/stable-diffusion-v3-5-large-turbo-GGUF:FP16`
   - `hf.co/gpustack/stable-diffusion-v3-5-large-turbo-GGUF:stable-diffusion-v3-5-large-turbo-Q4_0.gguf`

## 配置选项

| <div style="width:180px">选项</div> | <div style="width:100px">默认值</div> | 描述                                                                                 |
| ----------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------- |
| `--size` 值                      | `512x512`                              | 要生成的图像尺寸，以 `宽度x高度` 的形式指定。                                 |
| `--sampler` 值                   | `euler`                                | 采样方法。选项包括：euler_a、euler、heun、dpm2、dpm++2s_a、dpm++2m、lcm 等。 |
| `--sample-steps` 值              | (空)                                | 采样步数。                                                                   |
| `--cfg-scale` 值                 | (空)                                | 无分类器引导比例，用于平衡提示词遵循度和创造性。               |
| `--seed` 值                      | (空)                                | 随机数生成的种子。用于重现性。                              |
| `--negative-prompt` 值           | (空)                                | 用于避免在图像中出现的内容的文本提示词。                                                 |
| `--output` 值                    | (空)                                | 保存生成图像的路径。                                                           |
| `--show`                            | `False`                                | 如果为 True，则在默认图像查看器中打开生成的图像。                             |
| `-d`, `--debug`                     | `False`                                | 启用调试模式。                                                                          | 