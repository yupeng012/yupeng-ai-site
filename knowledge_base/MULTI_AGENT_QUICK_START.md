# OpenClaw 多智能体快速配置

**✅ 可以添加多个智能体！**

---

## 🎯 当前状态

**现有智能体：**
- main (默认) - 🐟 小鱼儿

**可以创建的智能体：**
- stock-analyst - 📊 股票分析师
- code-assistant - 💻 编程助手
- doc-assistant - 📝 文档助手
- data-analyst - 📈 数据分析师
- study-assistant - 🎓 学习助手

---

## 🚀 快速创建智能体

### 创建股票分析智能体

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

# 3. 配置路由
openclaw agents add-binding stock-analyst \
  --channel telegram \
  --keywords "股票,选股,持仓,买入,卖出,分析"

# 4. 验证配置
openclaw agents show stock-analyst
```

### 创建编程助手智能体

```bash
# 1. 创建智能体
openclaw agents add code-assistant \
  --model glm/z-ai/glm4.7 \
  --workspace ~/.openclaw/workspace/code \
  --identity "💻 编程助手" \
  --description "专业的代码编写和调试助手"

# 2. 配置路由
openclaw agents add-binding code-assistant \
  --channel telegram \
  --keywords "代码,编程,调试,函数,算法,Python"

# 3. 验证配置
openclaw agents show code-assistant
```

---

## 📱 智能体通信配置

### 为不同智能体配置不同的Telegram机器人

**股票分析智能体** (使用小鱼儿机器人):
```bash
openclaw config set agents.stock-analyst.channels.telegram.botToken "8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768"
openclaw config set agents.stock-analyst.channels.telegram.chatId "7847385399"
```

**编程助手智能体** (使用另一个机器人):
```bash
openclaw config set agents.code-assistant.channels.telegram.botToken "你的编程机器人Token"
openclaw config set agents.code-assistant.channels.telegram.chatId "你的Chat ID"
```

---

## 🎯 智能体路由规则

### 基于关键词自动路由

```bash
# 股票相关 → 股票分析智能体
openclaw agents add-binding stock-analyst \
  --channel telegram \
  --keywords "股票,选股,持仓,买入,卖出,分析,行情"

# 编程相关 → 编程助手智能体
openclaw agents add-binding code-assistant \
  --channel telegram \
  --keywords "代码,编程,调试,函数,算法,Python"

# 文档相关 → 文档助手智能体
openclaw agents add-binding doc-assistant \
  --channel telegram \
  --keywords "文档,写作,翻译,整理,报告"
```

---

## 📊 智能体管理命令

```bash
# 查看所有智能体
openclaw agents list

# 查看智能体详情
openclaw agents show stock-analyst

# 删除智能体
openclaw agents remove stock-analyst

# 切换默认智能体
openclaw agents set-default stock-analyst

# 查看智能体状态
openclaw agents status
```

---

## 🎨 智能体个性化

### 为每个智能体创建独立的身份文件

**股票分析智能体** (`~/.openclaw/workspace/stock/IDENTITY.md`):
```markdown
# IDENTITY.md - 股票分析师

- **Name**: 股票分析师
- **Creature**: 专业的股票分析AI
- **Vibe**: 专业、理性、数据驱动
- **Emoji**: 📊
- **Specialty**: 股票分析、选股、风险管理
```

**编程助手智能体** (`~/.openclaw/workspace/code/IDENTITY.md`):
```markdown
# IDENTITY.md - 编程助手

- **Name**: 编程助手
- **Creature**: 专业的编程AI
- **Vibe**: 技术导向、精确、高效
- **Emoji**: 💻
- **Specialty**: 代码编写、调试、优化
```

---

## 🔗 智能体协作

### 智能体间调用

在股票分析智能体中，可以调用编程助手来优化代码：

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

---

## 📝 推荐配置

### 基础配置（2个智能体）
1. **main** - 通用助手 🐟
2. **stock-analyst** - 股票分析师 📊

### 进阶配置（4个智能体）
1. **main** - 通用助手 🐟
2. **stock-analyst** - 股票分析师 📊
3. **code-assistant** - 编程助手 💻
4. **doc-assistant** - 文档助手 📝

### 高级配置（6个智能体）
1. **main** - 通用助手 🐟
2. **stock-analyst** - 股票分析师 📊
3. **code-assistant** - 编程助手 💻
4. **doc-assistant** - 文档助手 📝
5. **data-analyst** - 数据分析师 📈
6. **study-assistant** - 学习助手 🎓

---

## ⚠️ 注意事项

1. **资源管理**: 多个智能体会消耗更多资源
2. **配置冲突**: 确保不同智能体的配置不会冲突
3. **通信隔离**: 不同智能体应该使用独立的通信渠道
4. **数据隔离**: 每个智能体应该有独立的工作空间

---

**需要我帮你创建具体的智能体吗？** 🐟
