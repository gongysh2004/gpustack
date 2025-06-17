---
hide:
  - toc
---

# aiMindServe start

运行 aiMindServe 服务器或工作节点。

```bash
gpustack start [选项]
```

## 配置选项

### 通用选项

| <div style="width:180px">选项</div> | <div style="width:100px">默认值</div> | 描述                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--config-file` 值               | (空)                                | YAML 配置文件的路径。                                                                                                                                                                                                                                                                         |
| `-d` 值, `--debug` 值         | `False`                                | 启用调试模式。在 Windows 上不支持短标志 -d，因为该标志被 PowerShell 保留用于通用参数。                                                                                                                                                                 |
| `--data-dir` 值                  | (空)                                | 存储数据的目录。默认为操作系统特定的目录。                                                                                                                                                                                                                                                      |
| `--cache-dir` 值                 | (空)                                | 存储缓存（如模型文件）的目录。默认为 <data-dir>/cache。                                                                                                                                                                                                                           |
| `-t` 值, `--token` 值         | 自动生成                        | 用于添加工作节点的共享密钥。                                                                                                                                                                                                                                                                   |
| `--huggingface-token` 值         | (空)                                | 用于 Hugging Face Hub 认证的用户访问令牌。也可以通过 `HF_TOKEN` 环境变量配置。                                                                                                                                                                            |
| `--ollama-library-base-url` 值   | `https://registry.ollama.ai`           | Ollama 库的基础 URL。                                                                                                                                                                                                                                                                      |
| `--enable-ray`                      | `False`                                | 启用 Ray 以在多个工作节点上运行分布式 vLLM。仅在 Linux 上支持。                                                                                                                                                                                                             |
| `--ray-args` 值                  | (空)                                | 传递给 Ray 的参数。使用 `=` 避免 CLI 将 ray-args 识别为 aiMindServe 参数。可以多次使用以传递参数列表。例如：`--ray-args=--port=6379 --ray-args=--verbose`。更多详情请参见 [Ray 文档](https://docs.ray.io/en/latest/cluster/cli.html)。 |

### 服务器选项

| <div style="width:180px">选项</div> | <div style="width:100px">默认值</div> | 描述                                                                                                                                         |
| ----------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--host` 值                      | `0.0.0.0`                              | 服务器绑定的主机地址。                                                                                                                         |
| `--port` 值                      | `80`                                   | 服务器绑定的端口。                                                                                                                         |
| `--disable-worker`                  | `False`                                | 禁用内置工作节点。                                                                                                                            |
| `--bootstrap-password` 值        | 自动生成                        | 默认管理员用户的初始密码。                                                                                                        |
| `--database-url` 值              | `sqlite:///<data-dir>/database.db`     | 数据库的 URL。示例：postgresql://user:password@hostname:port/db_name 或 mysql://user:password@host:port/db_name                           |
| `--ssl-keyfile` 值               | (空)                                | SSL 密钥文件的路径。                                                                                                                           |
| `--ssl-certfile` 值              | (空)                                | SSL 证书文件的路径。                                                                                                                   |
| `--force-auth-localhost`            | `False`                                | 强制对来自本地主机（127.0.0.1）的请求进行身份验证。设置为 True 时，所有来自本地主机的请求都需要身份验证。 |
| `--disable-update-check`            | `False`                                | 禁用更新检查。                                                                                                                               |
| `--disable-openapi-docs`            | `False`                                | 禁用自动生成的 OpenAPI 文档端点（/docs 的 Swagger UI、/redoc 的 ReDoc 和 /openapi.json 的原始规范）。                    |
| `--model-catalog-file` 值        | (空)                                | 模型目录文件的路径或 URL。                                                                                                              |
| `--ray-port` 值                  | `40096`                                | Ray（GCS 服务器）的端口。在启用 Ray 时使用。                                                                                                 |
| `--ray-client-server-port` 值    | `40097`                                | Ray 客户端服务器的端口。在启用 Ray 时使用。                                                                                                |
| `--enable_cors`                     | `False`                                | 在服务器中启用 CORS。                                                                                                                              |
| `--allow-origins` 值             | `["*"]`                                | 允许进行跨源请求的来源列表。                                                                           |
| `--allow-credentials`               | `False`                                | 指示跨源请求应支持 cookie。                                                                                |
| `--allow-methods` 值             | `["GET", "POST"]`                      | 允许跨源请求的 HTTP 方法列表。                                                                            |
| `--allow-headers` 值             | `["Authorization", "Content-Type"]`    | 支持跨源请求的 HTTP 请求头列表。                                                                  |

### 工作节点选项

| <div style="width:180px">选项</div> | <div style="width:100px">默认值</div> | 描述                                                                                                                                                                                                                                                      |
| ----------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-s` 值, `--server-url` 值    | (空)                                | 要连接的服务器。                                                                                                                                                                                                                                            |
| `--worker-name` 值               | (空)                                | 工作节点的名称。默认使用主机名。                                                                                                                                                                                                            |
| `--worker-ip` 值                 | (空)                                | 工作节点的 IP 地址。默认自动检测。                                                                                                                                                                                                         |
| `--disable-metrics`                 | `False`                                | 禁用指标收集。                                                                                                                                                                                                                                                 |
| `--disable-rpc-servers`             | `False`                                | 禁用 RPC 服务器。                                                                                                                                                                                                                                             |
| `--metrics-port` 值              | `10151`                                | 暴露指标的端口。                                                                                                                                                                                                                                          |
| `--worker-port` 值               | `10150`                                | 工作节点绑定的端口。所有工作节点应使用一致的值。                                                                                                                                                                                              |
| `--service-port-range` 值        | `40000-40063`                          | 推理服务的端口范围，以 'N1-N2' 形式的字符串指定。范围的两端都包含在内。                                                                                                                                              |
| `--rpc-server-port-range` 值     | `40064-40095`                          | llama-box RPC 服务器的端口范围，以 'N1-N2' 形式的字符串指定。范围的两端都包含在内。                                                                                                                                           |
| `--ray-node-manager-port` 值     | `40098`                                | Ray 节点管理器的端口。在启用 Ray 时使用。                                                                                                                                                                                                              |
| `--ray-object-manager-port` 值   | `40099`                                | Ray 对象管理器的端口。在启用 Ray 时使用。                                                                                                                                                                                                            |
| `--ray-worker-port-range` 值     | `40100-40131`                          | Ray 工作进程的端口范围，以 'N1-N2' 形式的字符串指定。范围的两端都包含在内。                                                                                                                                            |
| `--log-dir` 值                   | (空)                                | 存储日志的目录。                                                                                                                                                                                                                                         |
| `--rpc-server-args` 值           | (空)                                | 传递给 RPC 服务器的参数。使用 `=` 避免 CLI 将 rpc-server-args 识别为服务器参数。可以多次使用以传递参数列表。示例：`--rpc-server-args=--verbose --rpc-server-args=--log-colors`              |
| `--system-reserved` 值           | `"{\"ram\": 2, \"vram\": 1}"`          | 系统在调度期间为工作节点保留的资源，以 GiB 为单位。默认保留 2 GiB RAM 和 1G VRAM。注意：'{\"memory\": 2, \"gpu_memory\": 1}' 也受支持，但已弃用，将在未来版本中移除。 |
| `--tools-download-base-url` 值   |                                        | 下载依赖工具的基础 URL。                                                                                                                                                                                                                       |
| `--enable-hf-transfer`              | `False`                                | 使用 hf_transfer 启用从 Hugging Face Hub 的更快下载。https://huggingface.co/docs/huggingface_hub/v0.29.3/package_reference/environment_variables#hfhubenablehftransfer                                                                           |

### 可用的环境变量

大多数选项都可以通过环境变量设置。环境变量以 `GPUSTACK_` 为前缀，并且使用大写。例如，`--data-dir` 可以通过 `GPUSTACK_DATA_DIR` 环境变量设置。

以下是可设置的其他环境变量：

| <div style="width:360px">选项</div> | 描述                                              |
| ----------------------------------- | -------------------------------------------------------- |
| `HF_ENDPOINT`                       | Hugging Face Hub 端点。例如：`https://hf-mirror.com` |

## 配置文件

在启动 aiMindServe 服务器或工作节点时，可以使用 YAML 格式的配置文件来配置启动选项。以下是一个完整的示例：

```yaml
# 通用选项
debug: false
data_dir: /path/to/data_dir
cache_dir: /path/to/cache_dir
token: mytoken
ollama_library_base_url: https://registry.mycompany.com
enable_ray: false
ray_args: ["--port=6379", "--verbose"]

# 服务器选项
host: 0.0.0.0
port: 80
disable_worker: false
database_url: postgresql://user:password@hostname:port/db_name
# database_url: mysql://user:password@host:port/db_name
ssl_keyfile: /path/to/keyfile
ssl_certfile: /path/to/certfile
force_auth_localhost: false
bootstrap_password: myadminpassword
disable_update_check: false
disable_openapi_docs: false
model_catalog_file: /path_or_url/to/model_catalog_file
ray_port: 40096
ray_client_server_port: 40097
enable_cors: false
allow_origins: ["*"]
allow_credentials: false
allow_methods: ["GET", "POST"]
allow_headers: ["Authorization", "Content-Type"]

# 工作节点选项
server_url: http://your_aimindserve_server_url
worker_name: myworker
worker_ip: 192.168.1.101
disable_metrics: false
disable_rpc_servers: false
metrics_port: 10151
worker_port: 10150
service_port_range: 40000-40063
rpc_server_port_range: 40064-40095
ray_node_manager_port: 40098
ray_object_manager_port: 40099
ray_worker_port_range: 40100-40131
log_dir: /path/to/log_dir
rpc_server_args: ["--verbose"]
system_reserved:
  ram: 2
  vram: 1
tools_download_base_url: https://mirror.mycompany.com
enable_hf_transfer: false
``` 