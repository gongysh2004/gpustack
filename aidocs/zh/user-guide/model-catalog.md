# 模型目录

模型目录是一个流行模型的索引，帮助你快速查找和部署模型。

## 浏览模型

你可以通过导航到 `目录` 页面浏览模型目录。你可以按名称和类别筛选模型。下图展示了模型目录页面：

![模型目录](../assets/model-catalog.png)

## 从目录部署模型

你可以通过点击模型卡片，从模型目录中部署模型。此时会弹出模型部署配置页面。你可以查看并自定义部署配置，然后点击 `保存` 按钮完成模型部署。

## 自定义模型目录

你可以通过 aiMindServe 服务器配置的 `--model-catalog-file` 参数，提供一个 YAML 文件来自定义模型目录。该参数支持本地文件路径或 URL。你可以参考[内置模型目录文件](https://github.com/gpustack/gpustack/blob/main/gpustack/assets/model-catalog.yaml)了解其结构。该文件包含模型集合列表，每个集合包含模型元数据和部署配置模板。

以下是模型目录文件中一个模型集合的示例：

```yaml
- name: Llama3.2
  description: Llama 3.2 多语言大模型（LLMs）集合，包含 1B 和 3B 规模的预训练和指令微调生成模型（文本输入/输出）。Llama 3.2 指令微调模型针对多语言对话场景进行了优化，适用于智能检索和摘要等任务，在常见行业基准上优于许多开源和闭源聊天模型。
  home: https://www.llama.com/
  icon: /static/catalog_icons/meta.png
  categories:
    - llm
  capabilities:
    - context/128k
    - tools
  sizes:
    - 1
    - 3
  licenses:
    - llama3.2
  release_date: "2024-09-25"
  order: 2
  templates:
    - quantizations:
        - Q3_K_L
        - Q4_K_M
        - Q5_K_M
        - Q6_K_L
        - Q8_0
        - f16
      source: huggingface
      huggingface_repo_id: bartowski/Llama-3.2-{size}B-Instruct-GGUF
      huggingface_filename: "*-{quantization}*.gguf"
      replicas: 1
      backend: llama-box
      cpu_offloading: true
      distributed_inference_across_workers: true
    - quantizations: ["BF16"]
      source: huggingface
      huggingface_repo_id: unsloth/Llama-3.2-{size}B-Instruct
      replicas: 1
      backend: vllm
      backend_parameters:
        - --enable-auto-tool-choice
        - --tool-call-parser=llama3_json
        - --chat-template={data_dir}/chat_templates/tool_chat_template_llama3.2_json.jinja
```

### 离线环境下使用模型目录

内置模型目录默认从 Hugging Face 或 ModelScope 获取模型。如果你在无互联网访问的离线环境下使用 aiMindServe，可以自定义模型目录，指定本地路径作为模型来源。示例如下：

```yaml
- name: Llama3.2
  description: Llama 3.2 多语言大模型（LLMs）集合，包含 1B 和 3B 规模的预训练和指令微调生成模型（文本输入/输出）。Llama 3.2 指令微调模型针对多语言对话场景进行了优化，适用于智能检索和摘要等任务，在常见行业基准上优于许多开源和闭源聊天模型。
  home: https://www.llama.com/
  icon: /static/catalog_icons/meta.png
  categories:
    - llm
  capabilities:
    - context/128k
    - tools
  sizes:
    - 1
    - 3
  licenses:
    - llama3.2
  release_date: "2024-09-25"
  order: 2
  templates:
    - quantizations:
        - Q3_K_L
        - Q4_K_M
        - Q5_K_M
        - Q6_K_L
        - Q8_0
        - f16
      source: local_path
      # 假设你已将所有 GGUF 模型文件放在 /path/to/the/model/directory
      local_path: /path/to/the/model/directory/Llama-3.2-{size}B-Instruct-{quantization}.gguf
      replicas: 1
      backend: llama-box
      cpu_offloading: true
      distributed_inference_across_workers: true
    - quantizations: ["BF16"]
      source: local_path
      # 假设你有 /path/to/Llama-3.2-1B-Instruct 和 /path/to/Llama-3.2-3B-Instruct 两个目录
      local_path: /path/to/Llama-3.2-{size}B-Instruct
      replicas: 1
      backend: vllm
      backend_parameters:
        - --enable-auto-tool-choice
        - --tool-call-parser=llama3_json
        - --chat-template={data_dir}/chat_templates/tool_chat_template_llama3.2_json.jinja
```

### 模板变量

部署配置中可用的模板变量如下：

- `{size}`：模型参数规模（以十亿为单位）。
- `{quantization}`：模型量化方式。
- `{data_dir}`：aiMindServe数据目录路径。
