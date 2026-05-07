# 🚀 OpenRouter API Key快速配置

## 一键配置

```bash
cd ~/.openclaw/workspace
python3 set_openrouter_key.py <your_api_key>
```

## 获取API Key

1. 访问 https://openrouter.ai/keys
2. 登录/注册账号
3. 创建API Key
4. 复制Key（格式：`sk-or-v1-xxxxxxxxxxxxx`）

## 验证配置

```bash
cd ~/.openclaw/workspace
python3 configure_api_keys.py
# 选择选项6测试连接
```

## 详细文档

- 📖 [完整配置指南](./API_KEYS_GUIDE.md)
- 📖 [OpenRouter使用说明](./OPENROUTER_SETUP.md)

## 支持的模型

- `anthropic/claude-3.5-sonnet` - Claude 3.5 Sonnet
- `anthropic/claude-3-opus` - Claude 3 Opus
- `openai/gpt-4-turbo` - GPT-4 Turbo
- `openai/gpt-4` - GPT-4
- `meta-llama/llama-3-70b-instruct` - Llama 3 70B

更多模型：https://openrouter.ai/models

---

**小鱼儿 🐟** | 2026-04-24
