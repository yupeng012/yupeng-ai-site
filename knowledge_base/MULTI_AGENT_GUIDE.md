# OpenClaw 多智能体配置指南

**配置时间**: 2026-04-14 19:14
**当前状态**: 1个智能体 (main)

---

## 🤖 什么是多智能体？

OpenClaw支持创建多个独立的智能体，每个智能体可以：
- 🎯 拥有不同的身份和个性
- 📁 使用独立的工作空间
- 🧠 配置不同的模型和参数
- 📱 连接不同的通信渠道
- 🔧 执行专门的任务

---

## 📋 智能体类型建议

### 1. 股票分析智能体
- **名称**: stock-analyst
- **功能**: 股票分析、选股、持仓管理
- **模型**: glm/z-ai/glm4.7
- **工作空间**: ~/.openclaw/workspace/stock
- **通信**: Telegram (小鱼儿机器人)

### 2. 编程助手智能体
- **名称**: code-assistant
- **功能**: 代码编写、调试、优化
- **模型**: glm/z-ai/glm4.7
- **工作空间**: ~/.openclaw/workspace/code
- **通信**: Telegram

### 3. 文档助手智能体
- **名称**: doc-assistant
- **功能**: 文档整理、写作、翻译
- **模型**: glm/z-ai/glm4.7
- **工作空间**: ~/.openclaw/workspace/docs
- **通信**: Telegram

### 4. 数据分析智能体
- **名称**: data-analyst
- **功能**: 数据处理、分析、可视化
- **模型**: glm/z-ai/glm4.7
- **工作空间**: ~/.openclaw/workspace/data
- **通信**: Telegram

### 5. 学习助手智能体
- **名称**: study-assistant
- **功能**: 学习辅导、知识整理
- **模型**: glm/z-ai/glm4.7
- **工作空间**: ~/.openclaw/workspace/study
- **通信**: Telegram

---

## 🔧 创建智能体方法

### 方法1: 使用命令行创建

```bash
# 创建股票分析智能体
openclaw agents add stock-analyst \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/stock \
  --identity "📊 股票分析师" \
  --description "专业的股票分析和选股助手"

# 创建编程助手智能体
openclaw agents add code-assistant \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/code \
  --identity "💻 编程助手" \
  --description "专业的代码编写和调试助手"

# 创建文档助手智能体
openclaw agents add doc-assistant \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/docs \
  --identity "📝 文档助手" \
  --description "专业的文档整理和写作助手"
```

### 方法2: 使用配置文件创建

创建配置文件 `~/.openclaw/agents/stock-analyst/agent.json`:

```json
{
  "id": "stock-analyst",
  "name": "股票分析师",
  "model": "glm/z-ai/glm4.7",
  "workspace": "~/.openclaw/workspace/stock",
  "identity": "📊 股票分析师",
  "description": "专业的股票分析和选股助手",
  "capabilities": {
    "tools": ["akshare", "pandas", "numpy", "matplotlib"],
    "channels": ["telegram"]
  }
}
```

然后运行：
```bash
openclaw agents add stock-analyst
```

---

## 📱 智能体通信配置

### 为不同智能体配置不同的Telegram机器人

#### 股票分析智能体
```bash
# 配置股票分析智能体使用小鱼儿机器人
openclaw config set agents.stock-analyst.channels.telegram.botToken "8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768"
openclaw config set agents.stock-analyst.channels.telegram.chatId "7847385399"
```

#### 编程助手智能体
```bash
# 配置编程助手智能体使用另一个机器人
openclaw config set agents.code-assistant.channels.telegram.botToken "你的编程机器人Token"
openclaw config set agents.code-assistant.channels.telegram.chatId "你的Chat ID"
```

---

## 🎯 智能体路由配置

### 基于关键词路由

```bash
# 股票相关消息路由到股票分析智能体
openclaw agents add-binding stock-analyst \
  --channel telegram \
  --keywords "股票,选股,持仓,买入,卖出,分析"

# 编程相关消息路由到编程助手智能体
openclaw agents add-binding code-assistant \
  --channel telegram \
  --keywords "代码,编程,调试,函数,算法,Python"

# 文档相关消息路由到文档助手智能体
openclaw agents add-binding doc-assistant \
  --channel telegram \
  --keywords "文档,写作,翻译,整理,报告"
```

### 基于群组路由

```bash
# 特定群组使用特定智能体
openclaw agents add-binding stock-analyst \
  --channel telegram \
  --group "股票交流群"

openclaw agents add-binding code-assistant \
  --channel telegram \
  --group "编程交流群"
```

---

## 📊 智能体管理命令

### 查看所有智能体
```bash
openclaw agents list
```

### 查看智能体详情
```bash
openclaw agents show stock-analyst
```

### 删除智能体
```bash
openclaw agents remove stock-analyst
```

### 切换默认智能体
```bash
openclaw agents set-default stock-analyst
```

### 查看智能体状态
```bash
openclaw agents status
```

---

## 🚀 实际应用场景

### 场景1: 股票分析自动化

**智能体**: stock-analyst
**功能**:
- 每日自动选股分析
- 持仓管理和提醒
- 技术指标计算
- 风险评估

**配置**:
```bash
# 创建智能体
openclaw agents add stock-analyst \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/stock

# 配置Telegram
openclaw config set agents.stock-analyst.channels.telegram.botToken "8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768"
openclaw config set agents.stock-analyst.channels.telegram.chatId "7847385399"

# 设置定时任务
openclaw cron add \
  --name "daily-stock-analysis" \
  --schedule "0 9 * * *" \
  --agent stock-analyst \
  --message "运行每日股票分析"
```

### 场景2: 代码审查和优化

**智能体**: code-assistant
**功能**:
- 代码审查
- 性能优化
- Bug修复
- 代码重构

**配置**:
```bash
# 创建智能体
openclaw agents add code-assistant \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/code

# 配置路由
openclaw agents add-binding code-assistant \
  --channel telegram \
  --keywords "代码,编程,调试,优化"
```

### 场景3: 文档自动生成

**智能体**: doc-assistant
**功能**:
- API文档生成
- 用户手册编写
- 技术文档整理
- 翻译服务

**配置**:
```bash
# 创建智能体
openclaw agents add doc-assistant \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/docs

# 配置路由
openclaw agents add-binding doc-assistant \
  --channel telegram \
  --keywords "文档,写作,翻译,报告"
```

---

## 🔗 智能体间协作

### 智能体调用其他智能体

在股票分析智能体中，可以调用编程助手智能体来优化代码：

```python
# 在stock-analyst的工作空间中
import subprocess

def optimize_code(code):
    """调用编程助手优化代码"""
    result = subprocess.run([
        "openclaw", "agents", "call", "code-assistant",
        "--message", f"请优化以下代码：\n\n{code}"
    ], capture_output=True, text=True)
    return result.stdout
```

### 智能体数据共享

不同智能体可以共享数据：

```bash
# 创建共享数据目录
mkdir -p ~/.openclaw/shared-data

# 在智能体配置中设置共享路径
openclaw config set agents.stock-analyst.sharedDataPath "~/.openclaw/shared-data"
openclaw config set agents.code-assistant.sharedDataPath "~/.openclaw/shared-data"
```

---

## 📝 智能体配置示例

### 股票分析智能体完整配置

```bash
# 1. 创建智能体
openclaw agents add stock-analyst \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/stock \
  --identity "📊 股票分析师" \
  --description "专业的股票分析和选股助手"

# 2. 配置Telegram
openclaw config set agents.stock-analyst.channels.telegram.enabled true
openclaw config set agents.stock-analyst.channels.telegram.botToken "8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768"
openclaw config set agents.stock-analyst.channels.telegram.chatId "7847385399"

# 3. 配置路由规则
openclaw agents add-binding stock-analyst \
  --channel telegram \
  --keywords "股票,选股,持仓,买入,卖出,分析,行情"

# 4. 设置定时任务
openclaw cron add \
  --name "daily-stock-analysis" \
  --schedule "0 9 * * *" \
  --agent stock-analyst \
  --message "运行每日股票分析"

# 5. 验证配置
openclaw agents show stock-analyst
```

---

## 🎨 智能体个性化配置

### 为每个智能体创建独立的身份文件

#### 股票分析智能体
创建 `~/.openclaw/workspace/stock/IDENTITY.md`:
```markdown
# IDENTITY.md - 股票分析师

- **Name**: 股票分析师
- **Creature**: 专业的股票分析AI
- **Vibe**: 专业、理性、数据驱动
- **Emoji**: 📊
- **Specialty**: 股票分析、选股、风险管理
```

#### 编程助手智能体
创建 `~/.openclaw/workspace/code/IDENTITY.md`:
```markdown
# IDENTITY.md - 编程助手

- **Name**: 编程助手
- **Creature**: 专业的编程AI
- **Vibe**: 技术导向、精确、高效
- **Emoji**: 💻
- **Specialty**: 代码编写、调试、优化
```

---

## 🔍 智能体监控和管理

### 查看智能体活动
```bash
# 查看所有智能体的活动状态
openclaw agents status

# 查看特定智能体的日志
tail -f ~/.openclaw/agents/stock-analyst/logs/agent.log
```

### 智能体性能监控
```bash
# 查看智能体资源使用
openclaw agents stats

# 查看智能体响应时间
openclaw agents performance
```

---

## ⚠️ 注意事项

1. **资源管理**: 多个智能体会消耗更多资源，注意系统性能
2. **配置冲突**: 确保不同智能体的配置不会冲突
3. **通信隔离**: 不同智能体应该使用独立的通信渠道
4. **数据隔离**: 每个智能体应该有独立的工作空间
5. **权限管理**: 为不同智能体配置适当的权限

---

## 🎯 推荐配置

### 基础配置（2个智能体）
1. **main** - 通用助手
2. **stock-analyst** - 股票分析专家

### 进阶配置（4个智能体）
1. **main** - 通用助手
2. **stock-analyst** - 股票分析专家
3. **code-assistant** - 编程助手
4. **doc-assistant** - 文档助手

### 高级配置（6个智能体）
1. **main** - 通用助手
2. **stock-analyst** - 股票分析专家
3. **code-assistant** - 编程助手
4. **doc-assistant** - 文档助手
5. **data-analyst** - 数据分析专家
6. **study-assistant** - 学习助手

---

**需要我帮你创建具体的智能体吗？** 🐟
