# Hermes Telegram Bot 配置指南

## 概述

Hermes Telegram Bot是一个基于NVIDIA Llama 3.1 405B模型的Telegram聊天机器人，可以通过Telegram与AI进行对话。

## 功能特性

- ✅ **智能对话** - 基于Llama 3.1 405B的强大推理能力
- ✅ **上下文记忆** - 记住对话历史，支持多轮对话
- ✅ **命令系统** - 支持多种命令控制
- ✅ **完全免费** - 使用NVIDIA免费API
- ✅ **长上下文** - 131K tokens上下文长度

## 系统要求

- Python 3.7+
- NVIDIA API Key
- Telegram Bot Token
- Telegram Chat ID

## 快速开始

### 1. 配置NVIDIA API

```bash
cd ~/.openclaw/workspace
python3 set_nvidia_key.py <your_nvidia_api_key>
```

### 2. 配置Telegram

编辑 `butler_config.py` 文件：

```python
BUTLER_CONFIG = {
    "enabled": True,
    "name": "管家",
    "telegram_chat_id": "你的Chat ID",  # 修改这里
    "telegram_bot_token": "你的Bot Token",  # 修改这里
    ...
}
```

### 3. 启动Bot

```bash
cd ~/.openclaw/workspace
./start_hermes_bot.sh
```

或者：

```bash
python3 hermes_telegram_bot.py
```

## 获取Telegram配置

### 获取Bot Token

1. 在Telegram中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按照提示创建bot
4. 复制获得的Bot Token

### 获取Chat ID

1. 在Telegram中搜索 `@userinfobot`
2. 发送任意消息
3. 复制获得的Chat ID

## 可用命令

### /start
开始使用Bot，显示欢迎信息。

### /help
显示帮助信息，包括所有可用命令。

### /clear
清除对话历史。

### /status
显示Bot状态信息，包括：
- 当前模型
- 对话数量
- 当前对话消息数
- 运行时间

## 使用示例

### 基本对话

```
你: 你好！
Bot: 你好！我是小鱼儿，一个基于NVIDIA Llama 3.1 405B的AI助手。有什么我可以帮助你的吗？

你: 请解释什么是量子计算？
Bot: 量子计算是一种利用量子力学原理进行计算的新型计算方式...
```

### 多轮对话

```
你: 什么是人工智能？
Bot: 人工智能是指由计算机系统所表现出的智能行为...

你: 它有哪些应用？
Bot: 人工智能有很多应用，包括：1. 自然语言处理 2. 计算机视觉 3. 机器学习...

你: 哪个应用最重要？
Bot: 这很难说，因为不同的应用在不同领域都很重要...
```

### 使用命令

```
你: /status
Bot: 🐟 Hermes Bot 状态

🤖 模型: meta/llama-3.1-405b-instruct
📊 对话数: 5
💬 当前对话: 12 条消息
⏰ 时间: 2026-04-24 13:00:00

✅ 运行正常
```

## 配置文件说明

### api_keys.json

存储API密钥配置：

```json
{
  "nvidia": {
    "api_key": "nvapi-xxxxxxxxxxxxx",
    "base_url": "https://integrate.api.nvidia.com/v1",
    "default_model": "meta/llama-3.1-405b-instruct"
  }
}
```

### butler_config.py

存储Telegram配置：

```python
BUTLER_CONFIG = {
    "enabled": True,
    "name": "管家",
    "telegram_chat_id": "7847385399",
    "telegram_bot_token": "8205207757:AAHBTHZXeRjDLZwzaO4uZzZZsNW6lqqwkdQ"
}
```

### conversations.json

存储对话历史：

```json
{
  "7847385399": [
    {
      "role": "user",
      "content": "你好！"
    },
    {
      "role": "assistant",
      "content": "你好！我是小鱼儿..."
    }
  ]
}
```

## 高级配置

### 修改系统提示

编辑 `hermes_telegram_bot.py` 文件：

```python
system_message = {
    "role": "system",
    "content": "你是一个有用的AI助手，名叫小鱼儿。你友好、专业、乐于助人。"
}
```

### 调整API参数

编辑 `hermes_telegram_bot.py` 文件：

```python
response = requests.post(
    f"{base_url}/chat/completions",
    headers=headers,
    json={
        "model": model,
        "messages": api_messages,
        "max_tokens": 1000,  # 调整最大输出长度
        "temperature": 0.7   # 调整创造性（0.0-1.0）
    },
    timeout=30
)
```

### 修改对话历史长度

编辑 `hermes_telegram_bot.py` 文件：

```python
# 限制对话历史长度
if len(self.conversations[str(chat_id)]) > 20:  # 修改这里
    self.conversations[str(chat_id)] = self.conversations[str(chat_id)][-20:]
```

## 故障排除

### 问题1: Bot无法启动

**解决方案**:
1. 检查Python是否安装：`python3 --version`
2. 检查配置文件是否存在
3. 检查NVIDIA API是否配置

### 问题2: 无法接收消息

**解决方案**:
1. 检查Bot Token是否正确
2. 检查Chat ID是否正确
3. 检查网络连接

### 问题3: API调用失败

**解决方案**:
1. 检查NVIDIA API Key是否有效
2. 检查网络连接
3. 查看日志文件

### 问题4: 对话历史丢失

**解决方案**:
1. 检查 `conversations.json` 文件权限
2. 确保文件可写
3. 检查磁盘空间

## 后台运行

### 使用nohup

```bash
cd ~/.openclaw/workspace
nohup python3 hermes_telegram_bot.py > hermes_bot.log 2>&1 &
```

### 使用screen

```bash
screen -S hermes_bot
cd ~/.openclaw/workspace
python3 hermes_telegram_bot.py
# 按 Ctrl+A 然后按 D 分离会话
```

### 使用systemd（推荐）

创建服务文件 `/etc/systemd/system/hermes-bot.service`：

```ini
[Unit]
Description=Hermes Telegram Bot
After=network.target

[Service]
Type=simple
User=wtueeq
WorkingDirectory=/Users/wtueeq/.openclaw/workspace
ExecStart=/usr/bin/python3 /Users/wtueeq/.openclaw/workspace/hermes_telegram_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start hermes-bot
sudo systemctl enable hermes-bot
```

## 监控和日志

### 查看日志

```bash
tail -f hermes_bot.log
```

### 检查服务状态

```bash
sudo systemctl status hermes-bot
```

### 重启服务

```bash
sudo systemctl restart hermes-bot
```

## 安全建议

1. **保护API Key** - 不要将API Key提交到版本控制系统
2. **限制访问** - 只允许授权用户使用Bot
3. **监控使用** - 定期检查API使用情况
4. **更新依赖** - 定期更新Python依赖包

## 性能优化

1. **使用缓存** - 缓存常见问题的答案
2. **限流** - 防止API滥用
3. **异步处理** - 使用异步IO提高性能
4. **负载均衡** - 多实例部署

## 相关资源

- [NVIDIA Build](https://build.nvidia.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Llama 3.1](https://llama.meta.com/llama-3-1/)

## 更新日志

- 2026-04-24: 创建Hermes Telegram Bot
- 2026-04-24: 集成NVIDIA API
- 2026-04-24: 添加对话历史功能
- 2026-04-24: 添加命令系统

## 联系支持

如有问题，请联系小鱼儿 🐟
