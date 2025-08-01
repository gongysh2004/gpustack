 # 兼容性检查

aiMindServe 在模型部署前会进行兼容性检查。该检查会提供模型与当前 aiMindServe 环境兼容性的详细信息。主要包括以下几项：

## 推理后端兼容性

检查所选推理后端是否与当前环境兼容，包括操作系统、GPU 和架构。

## 模型兼容性

判断所选推理后端是否支持该模型，包括模型格式和架构（如 `LlamaForCausalLM`、`Qwen3ForCausalLM` 等）。此检查基于内置推理后端及其支持的模型。如果使用自定义后端版本，则跳过此检查。

## 可调度性检查

评估模型是否可以在当前环境中调度，包括检查可用的 RAM、VRAM 及已配置的调度规则。

### 调度规则

调度规则（包括工作节点选择器、GPU 选择器和调度策略）用于判断模型能否在当前环境中被调度。

### 资源检查

aiMindServe 会估算模型所需资源，并与环境中可用资源进行对比。估算方法如下：

1. **GGUF 模型**aiMindServe 使用 [GGUF parser](https://github.com/gpustack/gguf-parser-go) 估算模型资源需求。
2. **其他模型**aiMindServe 使用如下公式估算 VRAM 占用：

$$
\text{VRAM} = \text{WEIGHT\_SIZE} \times 1.2 + \text{FRAMEWORK\_FOOTPRINT}
$$

- `WEIGHT_SIZE` 指模型权重文件的字节数。
- `FRAMEWORK_FOOTPRINT` 是框架的内存开销常量。例如，vLLM 在 CUDA 图上可能会占用数 GB VRAM。
- 1.2 倍系数为经验估算。详情可参考 [此说明](https://blog.eleuther.ai/transformer-math/#total-inference-memory)。

该公式仅为粗略估算，实际所需 VRAM 可能有所不同。通常它反映了最低需求。如果估算不足，用户可通过手动选择工作节点和 GPU，或调整高级后端参数实现更细粒度的调度。例如，vLLM 支持通过 `--tensor-parallel-size` 和 `--pipeline-parallel-size` 控制模型的 GPU 分配。
