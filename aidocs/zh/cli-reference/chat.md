---
hide:
  - toc
---

# aiMindServe chat

与大型语言模型进行对话。

```bash
gpustack chat model [prompt]
```

## 位置参数

| 名称   | 描述                                 |
| ------ | ------------------------------------------- |
| model  | 用于对话的模型。                  |
| prompt | 发送给模型的提示词。[可选] |

## 使用提示词进行一次性对话

如果提供了提示词，它将执行一次性推理。例如：

```bash
gpustack chat llama3 "tell me a joke."
```

示例输出：

```
Why couldn't the bicycle stand up by itself?

Because it was two-tired!
```

## 交互式对话

如果未提供 `prompt` 参数，您可以与大型语言模型进行交互式对话。例如：

```bash
gpustack chat llama3
```

示例输出：

```
>tell me a joke.
Here's one:

Why couldn't the bicycle stand up by itself?

(wait for it...)

Because it was two-tired!

Hope that made you smile!
>Do you have a better one?
Here's another one:

Why did the scarecrow win an award?

(think about it for a sec...)

Because he was outstanding in his field!

Hope that one stuck with you!

Do you want to hear another one?
>\quit
```

### 交互式命令

以下是交互式对话中可用的命令：

```
命令：
  \q 或 \quit - 退出对话
  \c 或 \clear - 清除提示词中的对话上下文
  \? 或 \h 或 \help - 打印此帮助信息
```

## 连接到外部 aiMindServe 服务器

如果您不是在服务器节点上运行 `gpustack chat`，或者如果您在自定义主机或端口上提供服务，您应该提供以下环境变量：

| 名称                | 描述                                              |
| ------------------- | -------------------------------------------------------- |
| GPUSTACK_SERVER_URL | aiMindServe 服务器的 URL，例如：`http://your_host_ip`。 |
| GPUSTACK_API_KEY    | aiMindServe API 密钥。                                        |
``` 