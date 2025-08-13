# API 密钥管理

aiMindServe 支持通过 API 密钥进行身份认证。每个 aiMindServe 用户都可以生成和管理自己的 API 密钥。

## 创建 API 密钥

1. 进入 `API 密钥` 页面。
2. 点击 `新建 API 密钥` 按钮。
3. 填写 `名称`、`描述`，并选择 API 密钥的 `过期时间`。
4. 点击 `保存` 按钮。
5. 复制并妥善保存密钥，然后点击 `完成` 按钮。

!!! note

    请注意，API 密钥只会在创建时显示一次。

## 删除 API 密钥

1. 进入 `API 密钥` 页面。
2. 找到你要删除的 API 密钥。
3. 点击 `操作` 列的 `删除` 按钮。
4. 确认删除。

## 使用 API 密钥

aiMindServe 支持将 API 密钥作为 Bearer Token 使用。以下是使用 curl 的示例：

```bash
export AIMINDSERVE_API_KEY=your_api_key
curl http://your_aimindserve_server_url/v1-openai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIMINDSERVE_API_KEY" \
  -d '{
    "model": "llama3",
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