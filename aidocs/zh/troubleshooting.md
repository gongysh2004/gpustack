# 故障排除

## 查看 aiMindServe 日志

如果您使用安装脚本或 Docker 安装了 aiMindServe，可以使用以下命令查看默认设置下的 aiMindServe 日志：

=== "Docker"

    ```bash
    docker logs -f aimindserve
    ```

## 配置日志级别

您可以通过设置 `--debug` 参数为 `gpustack start` 启用 DEBUG 日志级别。

您可以通过在服务器节点上运行以下命令来配置 aiMindServe 服务器的运行时日志级别：

```bash
curl -X POST http://localhost:10150/api/v1/log-level \
  -H "Content-Type: application/json" \
  -d '{"level": "DEBUG"}'
```

同样的方法也适用于 aiMindServe 工作节点：

```bash
curl -X POST http://localhost:10150/api/v1/log-level \
  -H "Content-Type: application/json" \
  -d '{"level": "DEBUG"}'
```

## 重置管理员密码

如果您忘记了管理员密码，可以使用以下命令重置：

```bash
gpustack reset-admin-password
```

如果默认端口已更改，请使用 `--server-url` 参数指定 aiMindServe URL。它必须在服务器本地运行并通过 `localhost` 访问：

```bash
gpustack reset-admin-password --server-url http://localhost:9090
```
