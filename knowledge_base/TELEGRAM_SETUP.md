# Telegram 配置指南

## 获取 Telegram Bot Token

1. 在 Telegram 中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按照提示给你的机器人起个名字（比如：`StockBot`）
4. BotFather 会给你一个 Token，格式类似：`123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

## 获取 Chat ID

1. 在 Telegram 中搜索你的机器人（比如：`StockBot`）
2. 给机器人发送任意消息（比如：`hello`）
3. 在浏览器中访问：`https://api.telegram.org/bot<你的TOKEN>/getUpdates`
4. 在返回的 JSON 中找到 `chat` -> `id`，这就是你的 Chat ID

## 配置环境变量

### 方法1：临时配置（当前会话有效）
```bash
export TELEGRAM_BOT_TOKEN="你的Bot Token"
export TELEGRAM_CHAT_ID="你的Chat ID"
```

### 方法2：永久配置（写入 ~/.zshrc）
```bash
echo 'export TELEGRAM_BOT_TOKEN="你的Bot Token"' >> ~/.zshrc
echo 'export TELEGRAM_CHAT_ID="你的Chat ID"' >> ~/.zshrc
source ~/.zshrc
```

### 方法3：直接修改 Python 脚本
编辑 `/Users/wtueeq/.openclaw/workspace/stock_terminal_nogui.py`，找到这两行：
```python
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
```

改为：
```python
TELEGRAM_BOT_TOKEN = "你的Bot Token"
TELEGRAM_CHAT_ID = "你的Chat ID"
```

## 测试配置

运行股票分析终端，如果配置正确，选股结果会自动发送到你的 Telegram：

```bash
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_nogui.py
```

## 注意事项

- Bot Token 和 Chat ID 是敏感信息，不要分享给他人
- 如果使用方法3直接修改脚本，确保不要将包含真实 Token 的脚本上传到公开仓库
- Telegram 消息有长度限制（4096字符），如果报告太长会被截断

---
配置完成后，每次运行选股工具，结果都会自动发送到你的 Telegram！
