# 安装要求

本页面描述了安装 aiMindServe 所需的软件和网络要求。

## Python 要求

aiMindServe 需要 Python 3.10 到 3.12 版本。

## 操作系统要求

aiMindServe 支持以下操作系统：

- [x] macOS
- [x] Windows
- [x] Linux

aiMindServe 已在以下操作系统上经过测试和验证：

| 操作系统  | 版本            |
| --------- | --------------- |
| Windows   | 10, 11          |
| macOS     | \>= 14          |
| Ubuntu    | \>= 20.04       |
| Debian    | \>= 11          |
| RHEL      | \>= 8           |
| Rocky     | \>= 8           |
| Fedora    | \>= 36          |
| OpenSUSE  | \>= 15.3 (leap) |
| OpenEuler | \>= 22.03       |

!!! note

    在 Linux 系统上安装 aiMindServe worker 要求 GLIBC 版本为 2.29 或更高。如果您的系统使用较低版本的 GLIBC，建议使用 `Docker 安装` 方式作为替代方案。

    使用以下命令检查 GLIBC 版本：

    ```
    ldd --version
    ```

### 支持的架构

aiMindServe 支持 **AMD64** 和 **ARM64** 架构，请注意以下几点：

- 在 Linux 和 macOS 上，当使用低于 3.12 的 Python 版本时，请确保安装的 Python 发行版与您的系统架构相对应。
- 在 Windows 上，请使用 AMD64 版本的 Python，因为某些依赖项的 wheel 包在 ARM64 上不可用。如果您使用 `conda` 等工具，这将自动处理，因为 conda 默认安装 AMD64 版本。

## 加速器运行时要求

aiMindServe 支持以下加速器：

- [x] NVIDIA CUDA（[计算能力](https://developer.nvidia.com/cuda-gpus) 6.0 及以上）
- [x] Apple Metal（M 系列芯片）安装请联系售后服务。
- [x] AMD ROCm
- [x] Ascend CANN
- [x] Hygon DTK
- [x] Moore Threads MUSA

在安装 aiMindServe 之前，请确保系统上已安装所有必要的驱动程序和库。

### NVIDIA CUDA

要使用 NVIDIA CUDA 作为加速器，请确保安装以下组件：

- [NVIDIA 驱动程序](https://www.nvidia.com/en-us/drivers/)
- [NVIDIA CUDA Toolkit 12](https://developer.nvidia.com/cuda-toolkit)（可选，非 Docker 安装时需要）
- [NVIDIA cuDNN 9](https://developer.nvidia.com/cudnn)（可选，非 Docker 安装时音频模型需要）
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit)（可选，Docker 安装时需要）

### AMD ROCm

要使用 AMD ROCm 作为加速器，请确保安装以下组件：

- [ROCm](https://rocm.docs.amd.com/en/docs-6.2.4/)

### Ascend CANN

要使用 Ascend CANN 作为加速器，请确保安装以下组件：

- [Ascend NPU 驱动和固件](https://www.hiascend.com/hardware/firmware-drivers/community)
- [Ascend CANN Toolkit 和 Kernels](https://www.hiascend.com/developer/download/community/result?module=cann&cann=8.1.RC1.beta1)（可选，非 Docker 安装时需要）

### Hygon DTK

要使用 Hygon DTK 作为加速器，请确保安装以下组件：

- [DCU 驱动](https://developer.sourcefind.cn/tool/)
- [DCU Toolkit](https://developer.sourcefind.cn/tool/)

### Moore Threads MUSA

要使用 Moore Threads MUSA 作为加速器，请确保安装以下组件：

- [MUSA SDK](https://developer.mthreads.com/sdk/download/musa)
- [MT Container Toolkits](https://developer.mthreads.com/sdk/download/CloudNative)（可选，Docker 安装时需要）

## 网络要求

### 网络架构

下图展示了 aiMindServe 的网络架构：

![aimindserve-network-architecture](../assets/aimindserve-network-architecture.png)

### 连接要求

为确保 aiMindServe 正常运行，需要以下网络连接：

**服务器到工作节点：** 服务器必须能够访问工作节点以代理推理请求。

**工作节点到服务器：** 工作节点必须能够访问服务器以注册自身并发送更新。

**工作节点到工作节点：** 用于跨多个工作节点的分布式推理

### 端口要求

aiMindServe 使用以下端口进行通信：

#### 服务器端口

| 端口    | 描述                                                              |
| ------- | ------------------------------------------------------------------------ |
| TCP 80  | aiMindServe UI 和 API 端点的默认端口                       |
| TCP 443 | 启用 TLS 时 aiMindServe UI 和 API 端点的默认端口 |

当启用 Ray 用于跨工作节点的分布式 vLLM 时，aiMindServe 服务器使用以下端口：

| Ray 端口  | 描述                         |
| --------- | ----------------------------------- |
| TCP 8265  | Ray 仪表板的默认端口      |
| TCP 40096 | Ray（GCS 服务器）的默认端口   |
| TCP 40097 | Ray 客户端服务器的默认端口  |
| TCP 40098 | Ray 节点管理器的默认端口   |
| TCP 40099 | Ray 对象管理器的默认端口 |

有关 Ray 端口的更多信息，请参阅 [Ray 文档](https://docs.ray.io/en/latest/ray-core/configure.html#ports-configurations)。

#### 工作节点端口

| 端口            | 描述                                    |
| --------------- | ---------------------------------------------- |
| TCP 10150       | aiMindServe 工作节点的默认端口           |
| TCP 10151       | 用于暴露指标的默认端口              |
| TCP 40000-40063 | 为推理服务分配的端口范围    |
| TCP 40064-40095 | 为 llama-box RPC 服务器分配的端口范围 |

当启用 Ray 用于跨工作节点的分布式 vLLM 时，aiMindServe 工作节点使用以下端口：

| Ray 端口        | 描述                         |
| --------------- | ----------------------------------- |
| TCP 40098       | Ray 节点管理器的默认端口   |
| TCP 40099       | Ray 对象管理器的默认端口 |
| TCP 40100-40131 | Ray 工作进程的端口范围 |

!!! note

    1. **支持异构集群。** 无论设备类型如何，只需指定 `--server-url` 和 `--token` 参数即可将其作为工作节点加入当前 aiMindServe集群。

    2. 本文档只描述用docker安装，需要其它安装方式，请联系售后服务。