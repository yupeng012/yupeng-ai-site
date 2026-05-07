# Telegram主要交流配置说明

**配置时间**: 2026-04-14 18:43
**配置状态**: ✅ 已完成

---

## 📱 Telegram配置信息

### 机器人信息
- **机器人名称**: 小鱼儿 (@yuzejing_bot)
- **Bot Token**: 8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768
- **Chat ID**: 7847385399
- **状态**: ✅ 已配置并启用

### 通知渠道优先级
1. **Telegram** - 主要通知渠道 ✅
2. **微信** - 备用通知渠道（可选）

---

## 📊 股票分析系统配置

### 主程序
- **文件位置**: `/Users/wtueeq/.openclaw/workspace/stock_terminal_telegram.py`
- **版本**: Telegram优先版
- **特点**: Telegram为主要通知渠道

### 定时任务
- **运行时间**: 每天 9:00
- **运行程序**: `stock_terminal_telegram.py`
- **状态**: ✅ 已配置

---

## 🔧 配置文件详情

### Telegram配置
```python
# Telegram配置（主要交流渠道）
TELEGRAM_BOT_TOKEN = "8214227298:AAFTBRnqs316zrivBvyEPuSCKUAWtIvE768"
TELEGRAM_CHAT_ID = "7847385399"
TELEGRAM_ENABLED = True  # Telegram为主要通知渠道
```

### 微信配置（备用）
```python
# 微信配置（备用渠道）
WECHAT_WEBHOOK_URL = os.getenv("WECHAT_WEBHOOK_URL", "")
WECHAT_ENABLED = False  # 微信为备用渠道
```

---

## 📱 Telegram通知功能

### 每日自动通知
- **时间**: 每天 9:00
- **内容**: 股票分析日报
- **格式**: 文本 + Excel文件链接

### 通知内容
1. **AI选股候选** (TOP 15)
   - 综合评分
   - 涨跌幅
   - 换手率
   - 风险评分
   - 技术指标

2. **模拟持仓状态**
   - 持仓股票
   - 盈亏情况
   - 操作建议

3. **Excel报告**
   - 候选股详情
   - 持仓详情
   - 技术指标
   - 汇总信息

---

## 🚀 使用方法

### 手动运行分析
```bash
# 运行Telegram优先版
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_telegram.py
```

### 查看定时任务状态
```bash
# 查看任务状态
launchctl list | grep stockterminal

# 手动启动任务
launchctl start com.stockterminal.daily

# 停止任务
launchctl stop com.stockterminal.daily
```

### 查看日志
```bash
# 查看主日志
tail -f ~/.stock_terminal/logs/terminal.log

# 查看定时任务日志
tail -f ~/.stock_terminal/logs/stdout.log
```

---

## 📊 生成的文件

### 每日报告
- **Excel报告**: `~/.stock_terminal/stock_report_YYYYMMDD.xlsx`
- **文本报告**: `~/.stock_terminal/daily_report.txt`
- **历史记录**: `~/.stock_terminal/history.csv`

### 日志文件
- **主日志**: `~/.stock_terminal/logs/terminal.log`
- **定时任务日志**: `~/.stock_terminal/logs/stdout.log`
- **错误日志**: `~/.stock_terminal/logs/stderr.log`

---

## 🎯 Telegram主要交流功能

### 实时通知
- ✅ 每日股票分析报告
- ✅ 买入信号提醒
- ✅ 止盈止损提醒
- ✅ 系统状态通知

### 交互功能
- 📱 通过Telegram接收分析结果
- 📊 查看Excel报告
- 📈 跟踪持仓状态
- 🔔 重要事件提醒

### 消息格式
```
🐟 股票分析日报

📊 AI选股候选 (TOP 15)
------------------------------------------------------------
排名   代码       名称       综合评分     涨跌幅      换手率      风险评分     RSI
------------------------------------------------------------
🔥 1  600152   维科技术     47.68    9.99     18.06    5.0      45.2
...

📈 模拟持仓
------------------------------------------------------------
代码       名称       买入价      最新价      盈亏%      盈亏金额       操作建议
------------------------------------------------------------
000001   平安银行     12.00    12.80    6.67     800.00     持有
...
```

---

## 🔧 配置管理

### 修改Telegram配置
编辑 `/Users/wtueeq/.openclaw/workspace/stock_terminal_telegram.py`:

```python
# 修改机器人Token
TELEGRAM_BOT_TOKEN = "你的新Token"

# 修改Chat ID
TELEGRAM_CHAT_ID = "你的Chat ID"

# 启用/禁用Telegram
TELEGRAM_ENABLED = True  # True=启用, False=禁用
```

### 修改定时任务时间
编辑 `~/Library/LaunchAgents/com.stockterminal.daily.plist`:

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>9</integer>      <!-- 修改小时 -->
    <key>Minute</key>
    <integer>0</integer>      <!-- 修改分钟 -->
</dict>
```

修改后重新加载:
```bash
launchctl unload ~/Library/LaunchAgents/com.stockterminal.daily.plist
launchctl load ~/Library/LaunchAgents/com.stockterminal.daily.plist
```

---

## 📞 技术支持

### 相关文件
- **主程序**: `/Users/wtueeq/.openclaw/workspace/stock_terminal_telegram.py`
- **高级版**: `/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py`
- **配置文档**: `/Users/wtueeq/.openclaw/workspace/TELEGRAM_SETUP.md`
- **定时任务**: `/Users/wtueeq/.openclaw/workspace/CRON_SETUP.md`

### 故障排除

#### Telegram消息未收到
1. 检查网络连接
2. 验证Bot Token和Chat ID
3. 查看日志文件
4. 测试Telegram API连接

#### 定时任务未运行
1. 检查任务状态: `launchctl list | grep stockterminal`
2. 查看错误日志: `tail -20 ~/.stock_terminal/logs/stderr.log`
3. 手动测试: `python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_telegram.py`

#### Excel文件未生成
1. 检查磁盘空间
2. 查看程序日志
3. 验证openpyxl库安装

---

## ✅ 配置验证清单

- [x] Telegram机器人已配置
- [x] Chat ID已设置
- [x] Bot Token已更新为小鱼儿
- [x] Telegram设为主要通知渠道
- [x] 定时任务已配置
- [x] 主程序已更新为Telegram优先版
- [x] Excel导出功能已启用
- [x] 每日自动通知已设置

---

## 🎉 配置完成

**Telegram已配置为主要交流渠道！**

从现在开始：
- 📱 每天早上9:00自动发送股票分析报告到Telegram
- 📊 包含完整的选股分析和持仓状态
- 📁 Excel报告自动生成
- 🔔 重要事件实时通知

**下次自动运行**: 明天早上9:00

**小鱼儿 🐟**
