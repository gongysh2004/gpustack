# 图像生成模型推荐参数

> aiMindServe 目前不支持非一体化（基础模型、文本编码器和VAE未合并）的GGUF图像生成模型。详情请参考支持的模型列表：
>
> - [Hugging Face 集合](https://huggingface.co/collections/gpustack/image-672dafeb2fa0d02dbe2539a9)
>
> - [ModelScope 集合](https://modelscope.cn/collections/Image-fab3d241f8a641)

图像生成模型的核心参数是实现理想输出的关键。这些参数包括 `Prompt`（提示词）、`Seed`（种子）、`Resolution`（分辨率）、`Sampler`（采样器）、`Scheduler`（调度器）、`Sampling Steps`（采样步数）和 `CFG scale`（CFG比例）。
不同模型的参数设置可能有所不同。为了快速上手并生成满意的图像，以下部分将提供一些参数配置的参考值。

## FLUX.1-dev

对于FLUX模型，建议禁用CFG（CFG=1）以获得更好的结果。

参考设置：

| 参数      | 值        |
| --------- | --------- |
| 尺寸      | 1024x1024 |
| 采样器    | euler     |
| 调度器    | discrete  |
| 步数      | 20        |
| CFG       | 1.0       |

推荐采样器：euler, heun, ipndm, ipndm_v

推荐调度器：discrete

✏️**试试看！**

```text
Prompt: A kangaroo holding a beer,wearing ski goggles and passionately singing silly songs.
尺寸: 1024x1024
采样器: euler
调度器: discrete
步数: 20
CFG: 1.0
种子: 838887451
```

![flux.1-dev](../assets/using-models/recommended-parameters-for-image-generation-models/flux.1-dev.png)

### 使用LoRA

**配置方法**：编辑模型 -> 高级 -> 后端参数 -> 添加 `--lora=<path/to/your/lora_file>`

![add-lora-file](../assets/using-models/recommended-parameters-for-image-generation-models/add-lora-file.png)

上排显示原始图像，下排显示使用LoRA生成的对应图像。

![flux.1-dev-lora](../assets/using-models/recommended-parameters-for-image-generation-models/flux.1-dev_lora.png)

!!! note

    LoRA目前是一个实验性功能。并非所有模型或LoRA文件都兼容。

## FLUX.1-schnell

对于FLUX模型，建议禁用CFG（CFG=1）以获得更好的结果。

参考设置：

| 参数      | 值        |
| --------- | --------- |
| 尺寸      | 1024x1024 |
| 采样器    | euler     |
| 调度器    | discrete  |
| 步数      | 2-4       |
| CFG       | 1.0       |

推荐采样器：euler, dpm++2mv2, ipndm_v

推荐调度器：discrete

✏️**试试看！**

```text
Prompt: A mischievous ferret with a playful grin squeezes itself into a large glass jar, surrounded by colorful candy. The jar sits on a wooden table in a cozy kitchen, and warm sunlight filters through a nearby window
尺寸: 1024x1024
采样器: euler
调度器: discrete
步数: 3
CFG: 1.0
种子: 1565801500
```

![flux.1-schnell](../assets/using-models/recommended-parameters-for-image-generation-models/flux.1-schnell.png)

## Stable-Diffusion-v3-5-Large

参考设置：

| 参数      | 值        |
| --------- | --------- |
| 尺寸      | 1024x1024 |
| 采样器    | euler     |
| 调度器    | discrete  |
| 步数      | 25        |
| CFG       | 4.5       |

推荐采样器：dpm++2m, ipndm, ipndm_v, dpm++2mv2, eluer, heun, dpm2

推荐调度器：discrete

✏️**试试看！**

```text
Prompt: Lucky flower pop art style with pink color scheme,happy cute girl character wearing oversized headphones and smiling while listening to music in the air with her eyes closed,vibrant colorful Japanese anime cartoon illustration with bold outlines and bright colors,colorful text "GPUStack" on top of background,high resolution,detailed,
Size: 1024x1024
Sampler: dpm++2m
Scheduler: discrete
Steps: 25
CFG: 5
Seed: 3520225659
```

![sd-v3_5-large](../assets/using-models/recommended-parameters-for-image-generation-models/sd-v3_5-large.png)

## Stable-Diffusion-v3-5-Large-Turbo

对于turbo模型，建议禁用CFG（CFG=1）以获得更好的结果。

参考设置：

| 参数      | 值                |
| --------- | ----------------- |
| 尺寸      | 1024x1024         |
| 采样器    | euler/dpm++2m     |
| 调度器    | discrete/exponential |
| 步数      | 5/15-20           |
| CFG       | 1.0               |

推荐采样器：euler, ipndm, ipndm_v, dpm++2mv2, heun, dpm2, dpm++2m

推荐调度器：discrete, karras, exponential

✏️**试试看！**

```text
Prompt: This dreamlike digital art captures a vibrant, kaleidoscopic bird in a lush rainforest
Size: 768x1024
Sampler: heun
Scheduler: karras
Steps: 15
CFG: 1.0
Seed: 2536656539
```

![sd-v3_5-large-turbo](../assets/using-models/recommended-parameters-for-image-generation-models/sd-v3_5-large-turbo.png)

## Stable-Diffusion-v3-5-Medium

参考设置：

| 参数      | 值       |
| --------- | -------- |
| 尺寸      | 768x1024 |
| 采样器    | euler    |
| 调度器    | discrete |
| 步数      | 28       |
| CFG       | 4.5      |

推荐采样器：euler, ipndm, ipndm_v, dpm++2mv2, heun, dpm2, dpm++2m

推荐调度器：discrete

✏️**试试看！**

```text
Prompt: Plush toy, a box of French fries, pink bag, long French fries, smiling expression, round eyes, smiling mouth, bright colors, simple composition, clean background, jellycat style,
Negative Prompt: ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2)
Size: 768x1024
Sampler: euler
Scheduler: discrete
Steps: 28
CFG: 4.5
种子: 3353126565
```

![sd-v3_5-medium](../assets/using-models/recommended-parameters-for-image-generation-models/sd-v3_5-medium.png)

## Stable-Diffusion-v3-Medium

参考设置：

| 参数      | 值        |
| --------- | --------- |
| 尺寸      | 1024x1024 |
| 采样器    | euler     |
| 调度器    | discrete  |
| 步数      | 25        |
| CFG       | 4.0       |

推荐采样器：euler, ipndm, ipndm_v, dpm++2mv2, heun, dpm2, dpm++2m

推荐调度器：discrete

✏️**试试看！**

```text
Prompt: A guitar crafted from a watermelon, realistic, close-up, ultra-HD, digital art, with smoke and ice cubes, soft lighting, dramatic stage effects of light and shadow, pastel aesthetic filter, time-lapse photography, macro photography, ultra-high resolution, perfect design composition, surrealism, hyper-imaginative, ultra-realistic, ultra-HD quality
Size: 768x1280
Sampler: euler
Scheduler: discrete
Steps: 30
CFG: 5.0
种子: 1937760054
```

!!! tip

    默认最大图像高度为1024。要增加高度，请编辑模型并在高级设置中添加后端参数 --image-max-height=1280。

![sd-v3-medium](../assets/using-models/recommended-parameters-for-image-generation-models/sd-v3-medium.png)

## SDXL-base-v1.0

参考设置：

| 参数      | 值        |
| --------- | --------- |
| 尺寸      | 1024x1024 |
| 采样器    | dpm++2m   |
| 调度器    | karras    |
| 步数      | 25        |
| CFG       | 5.0       |

推荐采样器：euler, ipndm, ipndm_v, dpm++2mv2, heun, dpm2, dpm++2m

推荐调度器：discrete, karras, exponential

✏️**试试看！**

```text
Prompt: Weeds blowing in the wind,By the seaside,Ultra-realistic,Majestic epic scenery,excessively splendid ancient rituals,vibrant,beautiful Eastern fantasy,bright sunshine,pink peach blossoms,daytime perspective.
Negative Prompt: ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),
尺寸: 768x1280
采样器: dpm++2m
调度器: exponential
步数: 30
CFG: 5.0
种子: 3754742591
```

![sdxl-base-v1.0](../assets/using-models/recommended-parameters-for-image-generation-models/sdxl-base-v1.0.png)

## Stable-Diffusion-v2-1-Turbo

对于turbo模型，建议禁用CFG（CFG=1）以获得更好的结果。

参考设置：

| 参数      | 值      |
| --------- | ------- |
| 尺寸      | 512x512 |
| 采样器    | euler_a |
| 调度器    | discrete |
| 步数      | 6       |
| CFG       | 1.0     |

推荐采样器：eluer_a, dmp++2s, lcm

推荐调度器：discrete, karras, exponential, ays, gits

✏️**试试看！**

```text
Prompt: A burger patty, with the bottom bun and lettuce and tomatoes.
Size: 512x512
Sampler: euler_a
Scheduler: discrete
Steps: 6
CFG: 1.0
Seed: 1375548153
```

![sd-v2_1-turbo](../assets/using-models/recommended-parameters-for-image-generation-models/sd-v2_1-turbo.png)

!!! note

    上述参数仅供参考。理想的设置可能因具体情况而异，应相应调整。
