# 快速开始

## 安装方法

有关安装或详细配置选项，请参阅[安装文档](installation/installation-requirements.md)。

## 开始使用

1. 运行并与 **llama3.2** 模型聊天：

```bash
gpustack chat llama3.2 "讲个笑话。"
```

2. 使用 **stable-diffusion-v3-5-large-turbo** 模型生成图像：

!!!tip

      此命令从 Hugging Face 下载模型（约 12GB）。下载时间取决于您的网络速度。确保您有足够的磁盘空间和显存（12GB）来运行模型。如果遇到问题，可以跳过此步骤，继续下一步。

```bash
gpustack draw hf.co/gpustack/stable-diffusion-v3-5-large-turbo-GGUF:stable-diffusion-v3-5-large-turbo-Q4_0.gguf \
"一个小黄人举着一个写着'aiMindServe'的牌子。背景充满了未来元素，如霓虹灯、电路板和全息显示。小黄人穿着科技主题的服装，可能带有 LED 灯或数字图案。牌子本身具有流线型现代设计，边缘发光。整体氛围高科技且充满活力，混合了深色和霓虹色。" \
--sample-steps 5 --show
```

命令完成后，生成的图像将出现在默认查看器中。您可以尝试修改提示词和 CLI 选项来自定义输出。

![生成的图像](../assets/quickstart-minion.png)

3. 在浏览器中打开 `http://your_host_ip` 访问 aiMindServe UI。使用用户名 `admin` 和默认密码登录 aiMindServe。您可以运行以下命令获取默认设置的密码：

=== "Linux"

    ```bash
    cat /var/lib/gpustack/initial_admin_password
    ```

1. 点击导航菜单中的 `Playground - Chat`。现在您可以在 UI 游乐场中与 LLM 聊天。

![游乐场截图](../assets/playground-screenshot.png)

4. 点击导航菜单中的 `API Keys`，然后点击 `New API Key` 按钮。

5. 填写 `Name` 并点击 `Save` 按钮。

6. 复制生成的 API 密钥并保存在安全的地方。请注意，您只能在创建时看到它一次。

7. 现在您可以使用 API 密钥访问 OpenAI 兼容的 API。例如，使用 curl 如下：

```bash
export AIMINDSERVE_API_KEY=your_api_key
curl http://your_aimindserve_server_url/v1-openai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
  -d '{
    "model": "llama3.2",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "stream": true
  }'
```

## 清理

完成使用已部署的模型后，您可以转到 aiMindServe UI 中的 `Models` 页面并删除模型以释放资源。
