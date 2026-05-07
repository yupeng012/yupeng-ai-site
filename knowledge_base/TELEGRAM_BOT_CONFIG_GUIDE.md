# 🤖 智能体Telegram机器人配置指南

## 📋 配置步骤

### 第一步：创建Telegram机器人

1. **打开Telegram**
   - 在Telegram中搜索 @BotFather
   - 点击开始对话

2. **创建新机器人**
   - 发送 `/newbot` 命令
   - 按照提示输入机器人名称
   - 按照提示输入机器人用户名（必须以_bot结尾）

3. **获取Token**
   - BotFather会返回一个Token
   - 保存这个Token，后面会用到

### 第二步：为8个智能体创建机器人

需要为以下8个智能体分别创建机器人：

1. **股票分析智能体**
   - 机器人名称: 股票分析智能体
   - 机器人用户名: stock_analysis_agent_bot

2. **基本面分析智能体**
   - 机器人名称: 基本面分析智能体
   - 机器人用户名: fundamental_analysis_agent_bot

3. **监控智能体**
   - 机器人名称: 监控智能体
   - 机器人用户名: monitoring_agent_bot

4. **报告智能体**
   - 机器人名称: 报告智能体
   - 机器人用户名: report_agent_bot

5. **学习智能体**
   - 机器人名称: 学习智能体
   - 机器人用户名: learning_agent_bot

6. **决策智能体**
   - 机器人名称: 决策智能体
   - 机器人用户名: decision_agent_bot

7. **风险智能体**
   - 机器人名称: 风险智能体
   - 机器人用户名: risk_agent_bot

8. **通知智能体**
   - 机器人名称: 通知智能体
   - 机器人用户名: notification_agent_bot

### 第三步：创建Telegram群组

1. **创建群组**
   - 在Telegram中创建一个新群组
   - 群组名称: 传奇级别智能体交流群

2. **添加机器人到群组**
   - 将8个机器人全部添加到群组
   - 确保所有机器人都有发送消息的权限

3. **获取群组ID**
   - 在群组中发送一条消息
   - 使用Telegram API获取群组ID
   - 保存群组ID，后面会用到

### 第四步：配置机器人Token

编辑 `agent_group_chat.py` 文件，将以下Token替换为真实的Token：

```python
bots_config = [
    {
        'agent_id': 'stock_analysis',
        'agent_name': '股票分析智能体',
        'agent_type': 'analysis',
        'bot_token': 'YOUR_STOCK_ANALYSIS_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'fundamental_analysis',
        'agent_name': '基本面分析智能体',
        'agent_type': 'fundamental',
        'bot_token': 'YOUR_FUNDAMENTAL_ANALYSIS_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'monitoring',
        'agent_name': '监控智能体',
        'agent_type': 'monitoring',
        'bot_token': 'YOUR_MONITORING_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'report',
        'agent_name': '报告智能体',
        'agent_type': 'report',
        'bot_token': 'YOUR_REPORT_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'learning',
        'agent_name': '学习智能体',
        'agent_type': 'learning',
        'bot_token': 'YOUR_LEARNING_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'decision',
        'agent_name': '决策智能体',
        'agent_type': 'decision',
        'bot_token': 'YOUR_DECISION_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'risk',
        'agent_name': '风险智能体',
        'agent_type': 'risk',
        'bot_token': 'YOUR_RISK_BOT_TOKEN'  # 替换为真实Token
    },
    {
        'agent_id': 'notification',
        'agent_name': '通知智能体',
        'agent_type': 'notification',
        'bot_token': 'YOUR_NOTIFICATION_BOT_TOKEN'  # 替换为真实Token
    }
]
```

### 第五步：配置群组ID

编辑 `agent_group_chat.py` 文件，将群组ID替换为真实的群组ID：

```python
# 创建群组
group_id = "YOUR_GROUP_ID"  # 替换为真实群组ID
group_name = "传奇级别智能体交流群"
chat_system.create_group(group_id, group_name)
```

### 第六步：测试机器人

1. **运行系统**
   ```bash
   python3 agent_group_chat.py
   ```

2. **检查Telegram群组**
   - 查看群组中是否有机器人发送的消息
   - 确认所有机器人都能正常工作

3. **测试对话**
   - 在群组中发送消息
   - 观察机器人的回应
   - 确认交流功能正常

## 🎯 高级配置

### 设置机器人命令

可以为每个机器人设置自定义命令：

```python
# 在AgentBot类中添加
def set_commands(self):
    """设置机器人命令"""
    commands = [
        ('analyze', '分析股票'),
        ('report', '生成报告'),
        ('learn', '学习新知识'),
        ('help', '帮助')
    ]
    # 使用Telegram API设置命令
```

### 设置机器人描述

可以为每个机器人设置描述：

```python
# 在AgentBot类中添加
def set_description(self):
    """设置机器人描述"""
    description = f"""
我是{self.agent_name}，传奇级别智能体。

我的能力：
{', '.join(self.capabilities)}

我可以帮你：
• 分析股票
• 提供决策
• 学习新知识
• 生成报告
    """.strip()
    # 使用Telegram API设置描述
```

### 设置机器人头像

可以为每个机器人设置头像：

```python
# 在AgentBot类中添加
def set_avatar(self, avatar_path):
    """设置机器人头像"""
    # 使用Telegram API设置头像
    pass
```

## 🔧 故障排除

### 机器人无法发送消息

**问题**: 机器人无法在群组中发送消息

**解决方案**:
1. 检查机器人Token是否正确
2. 检查机器人是否被添加到群组
3. 检查机器人是否有发送消息的权限
4. 检查网络连接是否正常

### 机器人无法接收消息

**问题**: 机器人无法接收群组中的消息

**解决方案**:
1. 检查机器人是否启用了Webhook
2. 检查机器人是否设置了正确的Webhook URL
3. 检查服务器是否正常运行
4. 检查防火墙设置

### 机器人响应缓慢

**问题**: 机器人响应速度很慢

**解决方案**:
1. 优化代码逻辑
2. 使用异步处理
3. 增加服务器资源
4. 使用缓存机制

## 📚 参考资料

- [Telegram Bot API文档](https://core.telegram.org/bots/api)
- [python-telegram-bot库](https://github.com/python-telegram-bot/python-telegram-bot)
- [Telethon库](https://docs.telethon.dev/)

## 🎯 总结

按照以上步骤配置完成后，你将拥有：

✅ 8个传奇级别智能体机器人  
✅ 1个智能体交流群组  
✅ 完整的智能体交流系统  
✅ 真实的智能体协作能力

智能体可以在群组中：
- 发送消息
- 互相回应
- 讨论分析结果
- 分享学习心得
- 协作完成任务

---

**配置完成后，智能体将真正实现群组交流协作！** 🐟
