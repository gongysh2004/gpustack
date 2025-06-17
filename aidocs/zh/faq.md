# 常见问题（FAQ）

## 支持矩阵

### 混合集群支持

支持 Linux、Windows 和 macOS 节点的混合部署，以及 x86_64 和 arm64 架构。此外，还支持多种 GPU，包括 NVIDIA、Apple Metal、AMD、昇腾、海光和摩尔线程。

### 分布式推理支持

**单节点多卡**

- [x] llama-box（不支持图像生成模型）
- [x] vLLM
- [x] MindIE
- [ ] vox-box

**多节点多卡**

- [x] llama-box
- [x] vLLM
- [ ] MindIE

**异构节点多卡**

- [x] llama-box

!!! tip

    相关文档：

    **vLLM**：[分布式推理与服务](https://docs.vllm.ai/en/latest/serving/distributed_serving.html)

    **llama-box**：[llama.cpp 分布式 LLM 推理](https://github.com/ggml-org/llama.cpp/tree/master/examples/rpc)

## 安装

### 如何更改 aiMindServe 默认端口？

aiMindServe 服务器默认使用 80 端口。你可以通过以下方式修改：

**Docker 安装**

在 `docker run` 命令末尾添加 `--port` 参数，如下：

```bash
docker run -d --name aimindserve \
    --restart=unless-stopped \
    --gpus all \
    --network=host \
    --ipc=host \
    -v aimindserve-data:/var/lib/aimindserve \
    aimindserve/aimindserve \
    --port 9090
```


### 如何更改注册的 worker 名称？

运行 aiMindServe 时通过 `--worker-name` 参数自定义 worker 名称：



**Docker 安装**

在 `docker run` 命令末尾添加 `--worker-name` 参数，如下：

```bash
docker run -d --name aimindserve \
    --restart=unless-stopped \
    --gpus all \
    --network=host \
    --ipc=host \
    -v aimindserve-data:/var/lib/aimindserve \
    aimindserve/aimindserve \
    --worker-name New-Name
```


### 如何更改注册的 worker IP？

运行 aiMindServe 时通过 `--worker-ip` 参数自定义 worker IP：



**Docker 安装**

在 `docker run` 命令末尾添加 `--worker-ip` 参数，如下：

```bash
docker run -d --name aimindserve \
    --restart=unless-stopped \
    --gpus all \
    --network=host \
    --ipc=host \
    -v aimindserve-data:/var/lib/aimindserve \
    aimindserve/aimindserve \
    --worker-ip xx.xx.xx.xx
```

