# 图像生成 API

aiMindServe 在运行扩散模型时，提供基于提示词和/或输入图片的图像生成 API。

!!! note

    图像生成 API 仅在使用 [llama-box](./inference-backends.md#llama-box) 推理后端时可用。

## 支持的模型

以下模型可用于图像生成：

!!! tip

    请使用 aiMindServe 提供的已转换 GGUF 模型。详情请查看模型链接。

- stabilityai/stable-diffusion-3.5-large-turbo [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v3-5-large-turbo-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v3-5-large-turbo-GGUF)
- stabilityai/stable-diffusion-3.5-large [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v3-5-large-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v3-5-large-GGUF)
- stabilityai/stable-diffusion-3.5-medium [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v3-5-medium-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v3-5-medium-GGUF)
- stabilityai/stable-diffusion-3-medium [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v3-medium-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v3-medium-GGUF)
- TencentARC/FLUX.1-mini [[Hugging Face]](https://huggingface.co/gpustack/FLUX.1-mini-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/FLUX.1-mini-GGUF)
- Freepik/FLUX.1-lite [[Hugging Face]](https://huggingface.co/gpustack/FLUX.1-lite-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/FLUX.1-lite-GGUF)
- black-forest-labs/FLUX.1-dev [[Hugging Face]](https://huggingface.co/gpustack/FLUX.1-dev-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/FLUX.1-dev-GGUF)
- black-forest-labs/FLUX.1-schnell [[Hugging Face]](https://huggingface.co/gpustack/FLUX.1-schnell-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/FLUX.1-schnell-GGUF)
- stabilityai/sdxl-turbo [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-xl-1.0-turbo-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-xl-1.0-turbo-GGUF)
- stabilityai/stable-diffusion-xl-refiner-1.0 [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-xl-refiner-1.0-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-xl-refiner-1.0-GGUF)
- stabilityai/stable-diffusion-xl-base-1.0 [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-xl-base-1.0-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-xl-base-1.0-GGUF)
- stabilityai/sd-turbo [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v2-1-turbo-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v2-1-turbo-GGUF)
- stabilityai/stable-diffusion-2-1 [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v2-1-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v2-1-GGUF)
- stable-diffusion-v1-5/stable-diffusion-v1-5 [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v1-5-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v1-5-GGUF)
- CompVis/stable-diffusion-v1-4 [[Hugging Face]](https://huggingface.co/gpustack/stable-diffusion-v1-4-GGUF), [[ModelScope]](https://modelscope.cn/models/gpustack/stable-diffusion-v1-4-GGUF)

## API 详情

图像生成 API 遵循 OpenAI API 规范。在 OpenAI 的图像生成 API aiMindServe 进行了扩展，提供了更多功能。

### 创建图片

#### 流式返回

该 API 支持流式响应，可实时返回生成进度。要启用流式返回，请在请求体中设置 `stream` 参数为 `true`。示例：

```
REQUEST : (application/json)
{
  "n": 1,
  "response_format": "b64_json",
  "size": "512x512",
  "prompt": "A lovely cat",
  "quality": "standard",
  "stream": true,
  "stream_options": {
    "include_usage": true, // 返回用量信息
  }
}

RESPONSE : (text/event-stream)
data: {"created":1731916353,"data":[{"index":0,"object":"image.chunk","progress":10.0}], ...}
...
data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":50.0}], ...}
...
data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":100.0,"b64_json":"..."}], "usage":{"generation_per_second":...,"time_per_generation_ms":...,"time_to_process_ms":...}, ...}
data: [DONE]
```

#### 高级选项

该 API 支持更多参数以控制生成过程。可用选项如下：

```
REQUEST : (application/json)
{
  "n": 1,
  "response_format": "b64_json",
  "size": "512x512",
  "prompt": "A lovely cat",
  "sampler": "euler",      // 必填，采样方法，可选：euler_a;euler;heun;dpm2;dpm++2s_a;dpm++2m;dpm++2mv2;ipndm;ipndm_v;lcm
  "schedule": "default",   // 可选，调度器，可选：default;discrete;karras;exponential;ays;gits
  "seed": null,            // 可选，随机种子
  "cfg_scale": 4.5,        // 可选，采样时无分类器引导的 scale
  "sample_steps": 20,      // 可选，采样步数
  "negative_prompt": "",   // 可选，反向提示词
  "stream": true,
  "stream_options": {
    "include_usage": true, // 返回用量信息
  }
}

RESPONSE : (text/event-stream)
data: {"created":1731916353,"data":[{"index":0,"object":"image.chunk","progress":10.0}], ...}
...
data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":50.0}], ...}
...
data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":100.0,"b64_json":"..."}], "usage":{"generation_per_second":...,"time_per_generation_ms":...,"time_to_process_ms":...}, ...}
data: [DONE]
```

### 创建图片编辑

#### 流式返回

该 API 支持流式响应，可实时返回生成进度。要启用流式返回，请在请求体中设置 `stream` 参数为 `true`。示例：

```
REQUEST: (multipart/form-data)
n=1
response_format=b64_json
size=512x512
prompt="A lovely cat"
quality=standard
image=...                         // 必填
mask=...                          // 可选
stream=true
stream_options_include_usage=true // 返回用量信息

RESPONSE : (text/event-stream)
CASE 1: 输入图片合法
  data: {"created":1731916353,"data":[{"index":0,"object":"image.chunk","progress":10.0}], ...}
  ...
  data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":50.0}], ...}
  ...
  data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":100.0,"b64_json":"..."}], "usage":{"generation_per_second":...,"time_per_generation_ms":...,"time_to_process_ms":...}, ...}
  data: [DONE]
CASE 2: 输入图片非法
  error: {"code": 400, "message": "Invalid image", "type": "invalid_request_error"}
```

#### 高级选项

该 API 支持更多参数以控制生成过程。可用选项如下：

```
REQUEST: (multipart/form-data)
n=1
response_format=b64_json
size=512x512
prompt="A lovely cat"
image=...                         // 必填
mask=...                          // 可选
sampler=euler                     // 必填，采样方法，可选：euler_a;euler;heun;dpm2;dpm++2s_a;dpm++2m;dpm++2mv2;ipndm;ipndm_v;lcm
schedule=default                  // 可选，调度器，可选：default;discrete;karras;exponential;ays;gits
seed=null                         // 可选，随机种子
cfg_scale=4.5                     // 可选，采样时无分类器引导的 scale
sample_steps=20                   // 可选，采样步数
negative_prompt=""                // 可选，反向提示词
stream=true
stream_options_include_usage=true // 返回用量信息

RESPONSE : (text/event-stream)
CASE 1: 输入图片合法
  data: {"created":1731916353,"data":[{"index":0,"object":"image.chunk","progress":10.0}], ...}
  ...
  data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":50.0}], ...}
  ...
  data: {"created":1731916371,"data":[{"index":0,"object":"image.chunk","progress":100.0,"b64_json":"..."}], "usage":{"generation_per_second":...,"time_per_generation_ms":...,"time_to_process_ms":...}, ...}
  data: [DONE]
CASE 2: 输入图片非法
  error: {"code": 400, "message": "Invalid image", "type": "invalid_request_error"}
```

## 用法示例

以下是图像生成 API 的使用示例：

### curl（创建图片）

```bash
export AIMINDSERVE_API_KEY=your_api_key
curl http://your_aimindserve_server_url/v1-openai/image/generate \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
    -d '{
        "n": 1,
        "response_format": "b64_json",
        "size": "512x512",
        "prompt": "A lovely cat",
        "quality": "standard",
        "stream": true,
        "stream_options": {
        "include_usage": true
        }
    }'
```

### curl（图片编辑）

```bash
export AIMINDSERVE_API_KEY=your_api_key
curl http://your_gpustack_server_url/v1-openai/image/edit \
    -H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
    -F image="@otter.png" \
    -F mask="@mask.png" \
    -F prompt="A lovely cat" \
    -F n=1 \
    -F size="512x512"
``` 