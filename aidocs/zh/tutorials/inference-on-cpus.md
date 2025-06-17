# 在 CPU 上运行推理

aiMindServe 支持在 CPU 上进行推理，当 GPU 资源有限或模型大小超过可用 GPU 内存时提供了灵活性。以下是可用的 CPU 推理模式：

- **CPU+GPU 混合推理**：当显存容量不足时，通过将大型模型的部分内容卸载到 CPU 来实现部分加速。
- **纯 CPU 推理**：当没有 GPU 资源可用时，完全在 CPU 上运行。

!!! note

    使用 llama-box 后端时支持 CPU 推理。

要在部署时启用 CPU 卸载，请在部署配置中启用 `Allow CPU Offloading` 选项（此设置默认启用）。

![Allow CPU Offload](../assets/tutorials/inference-on-cpus/allow-cpu-offload.png)

部署后，您可以查看卸载到 CPU 的模型层数。

![CPU Offload](../assets/tutorials/inference-on-cpus/cpu-offload.png) 