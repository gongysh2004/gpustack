# 固定后端版本

生成式 AI 领域的推理引擎正在快速发展，以提升性能并解锁新能力。这种持续演进带来了令人兴奋的机遇，但也为模型兼容性和部署稳定性带来了挑战。

aiMindServe 允许你将[推理后端](./inference-backends.md)版本固定到特定发布版本，在保持最新进展和确保可靠运行环境之间取得平衡。此功能在以下场景尤为有用：

- 利用最新后端特性，无需等待 aiMindServe 升级。
- 锁定特定后端版本，保证现有模型兼容性。
- 针对不同需求的模型分配不同后端版本。

通过固定后端版本，你可以完全掌控推理环境，实现部署的灵活性与可预测性。

## 固定后端版本的自动安装

为简化部署，aiMindServe 支持在可行时自动安装固定的后端版本。具体流程取决于后端类型：

1. **预编译二进制包**  
   对于如 `llama-box` 这类后端，aiMindServe 会通过与启动时相同的机制下载指定版本。

!!! tip

    你可以通过 `--tools-download-base-url` [配置项](../cli-reference/start.md)自定义下载源。

2. **基于 Python 的后端**  
   对于如 `vLLM` 和 `vox-box` 这类后端，aiMindServe 使用 `pipx` 在隔离的 Python 环境中安装指定版本。

!!! tip

    - 请确保 worker 节点已安装 `pipx`。
    - 若 `pipx` 不在系统 PATH，可通过 `--pipx-path` [配置项](../cli-reference/start.md)指定其路径。

此自动化流程减少了人工干预，让你专注于模型部署和使用。

## 固定后端版本的手动安装

当自动安装不可行或不希望自动安装时，aiMindServe 也支持手动安装特定版本的推理后端。步骤如下：

1. **准备可执行文件**  
   安装后端可执行文件，或将其链接到 aiMindServe 的 bin 目录。默认位置为：

   - **Linux/macOS：** `/var/lib/gpustack/bin`
   - **Windows：** `$env:AppData\gpustack\bin`

!!! tip

    你可以通过 `--bin-dir` [配置项](../cli-reference/start.md)自定义 bin 目录。

2. **命名可执行文件**  
   确保可执行文件命名格式如下：

   - **Linux/macOS：** `<backend>_<version>`
   - **Windows：** `<backend>_<version>.exe`

例如，vLLM v0.7.3 版本的可执行文件在 Linux 下应命名为 `vllm_v0.7.3`。

按照上述步骤操作，你可以完全掌控后端安装流程，确保部署时使用正确的版本。 