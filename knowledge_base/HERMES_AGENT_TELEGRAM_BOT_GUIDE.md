# Hermes Agent Telegram Bot 配置指南

## 概述

Hermes Agent Telegram Bot是一个基于NVIDIA Llama 3.1 405B模型的Telegram聊天机器人，专门用于控制Hermes Agent，提供股票分析、投资建议等专业服务。

## Bot信息

- **Bot名称**: @newlittlerpig_bot
- **Bot Token**: 8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw
- **模型**: NVIDIA Llama 3.1 405B Instruct
- **上下文**: 131K tokens
- **费用**: 免费

## 功能特性

- ✅ **智能对话** - 基于Llama 3.1 405B的强大推理能力
- ✅ **上下文记忆** - 记住对话历史，支持多轮对话
- ✅ **命令系统** - 支持多种命令控制
- ✅ **股票分析** - 专业的股票分析和投资建议
- ✅ **报告生成** - 自动生成各类分析报告
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
    "telegram_bot_token": "8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw",  # 已配置
    ...
}
```

### 3. 启动Bot

```bash
cd ~/.openclaw/workspace
./start_hermes_agent_bot.sh
```

或者：

```bash
python3 hermes_agent_telegram_bot.py
```

## 获取Telegram Chat ID

### 方法1: 使用userinfobot

1. 在Telegram中搜索 `@userinfobot`
2. 发送任意消息
3. 复制获得的Chat ID

### 方法2: 使用API

```bash
curl https://api.telegram.org/bot8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw/getUpdates
```

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

### /analyze
股票分析功能。提供股票代码或公司名称，进行详细分析。

**示例**:
```
/analyze 002837
/analyze 英维克
```

**分析内容包括**:
- 基本面分析
- 技术面分析
- 风险评估
- 投资建议

### /report
生成报告功能。可以生成以下类型的报告：

1. 每日市场报告
2. 股票分析报告
3. 投资策略报告
4. 风险评估报告

## 使用示例

### 基本对话

```
你: 你好！
Bot: 你好！我是小鱼儿，一个基于NVIDIA Llama 3.1 405B的AI助手。有什么我可以帮助你的吗？

你: 请分析一下002837这只股票
Bot: 好的，让我为你分析002837英维克这只股票...

[详细分析内容]
```

### 股票分析

```
你: /analyze 002837
Bot: 📊 股票分析功能

请提供股票代码或公司名称，我将为你进行详细分析。

分析内容包括：
• 基本面分析
• 技术面分析
• 风险评估
• 投资建议

你: 002837
Bot: 📊 002837 英维克 分析报告

[详细分析内容]
```

### 生成报告

```
你: /report
Bot: 📋 生成报告功能

我可以为你生成以下类型的报告：

1. 每日市场报告
2. 股票分析报告
3. 投资策略报告
4. 风险评估报告

请告诉我你需要哪种报告。

你: 生成002837的投资策略报告
Bot: 📋 002837 投资策略报告

[详细报告内容]
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
    "telegram_bot_token": "8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw"
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

编辑 `hermes_agent_telegram_bot.py` 文件：

```python
system_message = {
    "role": "system",
    "content": """你是Hermes Agent，一个专业的AI助手。你的名字叫小鱼儿。

你的主要职责：
1. 帮助用户解决问题
2. 提供专业的建议和分析
3. 协助用户进行决策
4. 保持友好和专业的态度

你擅长：
- 股票分析和投资建议
- 技术分析和基本面分析
- 风险管理和策略制定
- 数据分析和报告生成

请用专业、准确、友好的方式回答用户的问题。"""
}
```

### 调整API参数

编辑 `hermes_agent_telegram_bot.py` 文件：

```python
response = requests.post(
    f"{base_url}/chat/completions",
    headers=headers,
    json={
        "model": model,
        "messages": api_messages,
        "max_tokens": 1500,  # 调整最大输出长度
        "temperature": 0.7   # 调整创造性（0.0-1.0）
    },
    timeout=30
)
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
4. 确保已启动Bot

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
nohup python3 hermes_agent_telegram_bot.py > hermes_agent_bot.log 2>&1 &
```

### 使用screen

```bash
screen -S hermes_agent_bot
cd ~/.openclaw/workspace
python3 hermes_agent_telegram_bot.py
# 按 Ctrl+A 然后按 D 分离会话
```

### 使用systemd（推荐）

创建服务文件 `/etc/systemd/system/hermes-agent-bot.service`：

```ini
[Unit]
Description=Hermes Agent Telegram Bot
After=network.target

[Service]
Type=simple
User=wtueeq
WorkingDirectory=/Users/wtueeq/.openclaw/workspace
ExecStart=/usr/bin/python3 /Users/wtueeq/.openclaw/workspace/hermes_agent_telegram_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start hermes-agent-bot
sudo systemctl enable hermes-agent-bot
```

## 监控和日志

### 查看日志

```bash
tail -f hermes_agent_bot.log
```

### 检查服务状态

```bash
sudo systemctl status hermes-agent-bot
```

### 重启服务

```bash
sudo systemctl restart hermes-agent-bot
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

- 2026-04-24: 创建Hermes Agent Telegram Bot
- 2026-04-24: 集成NVIDIA API
- 2026-04-24: 添加股票分析功能
- 2026-04-24: 添加报告生成功能
- 2026-04-24: 配置@newlittlerpig_bot

## 联系支持

如有问题，请联系小鱼儿 🐟
