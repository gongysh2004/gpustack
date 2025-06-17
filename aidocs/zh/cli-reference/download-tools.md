---
hide:
  - toc
---

# aiMindServe download-tools

下载依赖工具，包括 llama-box、gguf-parser 和 fastfetch。

```bash
gpustack download-tools [选项]
```

## 配置选项

| <div style="width:180px">选项</div> | <div style="width:100px">默认值</div> | 描述                                                                        |
| ----------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------- |
| `----tools-download-base-url` 值 | (空)                                | 下载依赖工具的基础 URL。                                             |
| `--save-archive` 值              | (空)                                | 将下载的工具保存为 tar 归档文件的路径。                                    |
| `--load-archive` 值              | (空)                                | 从 tar 归档文件加载工具，而不是下载。          |
| `--system` 值                    | 默认为当前操作系统。             | 要下载工具的操作系统。选项：`linux`、`windows`、`macos`。      |
| `--arch` 值                      | 默认为当前架构。   | 要下载工具的架构。选项：`amd64`、`arm64`。                     |
| `--device` 值                    | 默认为当前设备。         | 要下载工具的设备。选项：`cuda`、`mps`、`npu`、`dcu`、`musa`、`cpu`。 | 