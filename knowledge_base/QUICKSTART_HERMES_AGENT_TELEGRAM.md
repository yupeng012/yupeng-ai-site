# 🚀 Hermes Agent Telegram Bot 快速开始

## Bot信息

- **Bot名称**: @newlittlerpig_bot
- **Bot Token**: 8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw
- **模型**: NVIDIA Llama 3.1 405B Instruct

## 一键启动

```bash
cd ~/.openclaw/workspace
./start_hermes_agent_bot.sh
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
    "telegram_bot_token": "8166589169:AAH6vL5b34aI7HCdnczsk7jCSVbmPBp8WZw"  # 已配置
}
```

## 使用方法

### 启动Bot

```bash
cd ~/.openclaw/workspace
python3 hermes_agent_telegram_bot.py
```

### 在Telegram中使用

1. 找到 @newlittlerpig_bot
2. 发送 `/start` 开始
3. 发送消息与AI对话

## 可用命令

- `/start` - 开始使用
- `/help` - 查看帮助
- `/clear` - 清除对话历史
- `/status` - 查看状态
- `/analyze` - 股票分析
- `/report` - 生成报告

## 对话示例

### 基本对话

```
你: 你好！
Bot: 你好！我是小鱼儿，一个基于NVIDIA Llama 3.1 405B的AI助手。有什么我可以帮助你的吗？

你: 请分析一下002837这只股票
Bot: 好的，让我为你分析002837英维克这只股票...
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

## 后台运行

```bash
cd ~/.openclaw/workspace
nohup python3 hermes_agent_telegram_bot.py > hermes_agent_bot.log 2>&1 &
```

## 查看日志

```bash
tail -f hermes_agent_bot.log
```

## 停止Bot

```bash
# 查找进程
ps aux | grep hermes_agent_telegram_bot

# 停止进程
kill <PID>
```

## 详细文档

- 📖 [完整配置指南](./HERMES_AGENT_TELEGRAM_BOT_GUIDE.md)
- 📖 [NVIDIA配置指南](./NVIDIA_CONFIG_GUIDE.md)

## 特性

- ✅ 智能对话 - Llama 3.1 405B
- ✅ 上下文记忆 - 多轮对话
- ✅ 命令系统 - 6个命令
- ✅ 股票分析 - 专业分析
- ✅ 报告生成 - 自动报告
- ✅ 完全免费 - NVIDIA API
- ✅ 长上下文 - 131K tokens

## 专长领域

- 📊 股票分析和投资建议
- 📈 技术分析和基本面分析
- ⚠️ 风险管理和策略制定
- 📋 数据分析和报告生成

---

**小鱼儿 🐟** | 2026-04-24
