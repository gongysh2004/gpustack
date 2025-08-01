# 卸载


## Docker

如果您使用 Docker 安装了 aiMindServe，以下是卸载 aiMindServe 的示例命令。您可以根据您的设置进行修改：

```bash
# 删除容器
docker rm -f aimindserve
# 删除数据卷
docker volume rm aimindserve-data
```