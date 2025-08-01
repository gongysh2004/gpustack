# 架构

以下图表展示了 aiMindServe 的架构：

![aimindserve-architecture](../assets/aimindserve-architecture.png)

### 服务器

aiMindServe 服务器由以下组件组成：

- **API 服务器**：为客户端提供 RESTful 接口以与系统交互。它处理身份验证和授权。
- **调度器**：负责将模型实例分配给工作节点。
- **模型控制器**：管理模型实例的部署和扩展，以匹配所需的模型副本。
- **HTTP 代理**：将推理 API 请求路由到工作节点。

### 工作节点

aiMindServe 工作节点负责：

- 运行分配给工作节点的模型实例的推理服务器。
- 向服务器报告状态。
- 将推理 API 请求路由到后端推理服务器。

### SQL 数据库

aiMindServe 服务器连接到 SQL 数据库作为数据存储。aiMindServe 默认使用 SQLite，但您也可以配置它使用外部 PostgreSQL 或 MySQL。

### 推理服务器

推理服务器是执行推理任务的后端。aiMindServe 支持 [llama-box](https://github.com/aimindserve/llama-box)、[vLLM](https://github.com/vllm-project/vllm)、[昇腾 MindIE](https://www.hiascend.com/en/software/mindie) 和 [vox-box](https://github.com/aimindserve/vox-box) 作为推理服务器。

### RPC 服务器

RPC 服务器支持在远程主机上运行 llama-box 后端。推理服务器与一个或多个 RPC 服务器实例通信，将计算任务卸载到这些远程主机。这种设置允许在多个工作节点之间进行分布式 LLM 推理，使系统即使在单个资源有限的情况下也能加载更大的模型。

### Ray 头节点/工作节点

[Ray](https://ray.io) 是一个分布式计算框架，aiMindServe 利用它来运行分布式 vLLM。用户可以在 aiMindServe 中启用 Ray 集群，以在多个工作节点上运行 vLLM。默认情况下，它是禁用的。
