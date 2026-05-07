# 🚀 Hermes Telegram Bot 快速开始

## 一键启动

```bash
cd ~/.openclaw/workspace
./start_hermes_bot.sh
```

## 前置条件

### 1. NVIDIA API已配置 ✅

```bash
python3 check_nvidia_status.py
```

### 2. Telegram已配置 ✅

检查 `butler_config.py` 文件：

```python
BUTLER_CONFIG = {
    "telegram_chat_id": "7847385399",  # 你的Chat ID
    "telegram_bot_token": "8205207757:AAHBTHZXeRjDLZwzaO4uZzZZsNW6lqqwkdQ"  # 你的Bot Token
}
```

## 使用方法

### 启动Bot

```bash
cd ~/.openclaw/workspace
python3 hermes_telegram_bot.py
```

### 在Telegram中使用

1. 找到你的Bot
2. 发送 `/start` 开始
3. 发送消息与AI对话

## 可用命令

- `/start` - 开始使用
- `/help` - 查看帮助
- `/clear` - 清除对话历史
- `/status` - 查看状态

## 对话示例

```
你: 你好！
Bot: 你好！我是小鱼儿，一个基于NVIDIA Llama 3.1 405B的AI助手。有什么我可以帮助你的吗？

你: 请解释什么是量子计算？
Bot: 量子计算是一种利用量子力学原理进行计算的新型计算方式...
```

## 后台运行

```bash
cd ~/.openclaw/workspace
nohup python3 hermes_telegram_bot.py > hermes_bot.log 2>&1 &
```

## 查看日志

```bash
tail -f hermes_bot.log
```

## 停止Bot

```bash
# 查找进程
ps aux | grep hermes_telegram_bot

# 停止进程
kill <PID>
```

## 详细文档

- 📖 [完整配置指南](./HERMES_TELEGRAM_BOT_GUIDE.md)
- 📖 [NVIDIA配置指南](./NVIDIA_CONFIG_GUIDE.md)

## 特性

- ✅ 智能对话 - Llama 3.1 405B
- ✅ 上下文记忆 - 多轮对话
- ✅ 命令系统 - 4个命令
- ✅ 完全免费 - NVIDIA API
- ✅ 长上下文 - 131K tokens

---

**小鱼儿 🐟** | 2026-04-24
