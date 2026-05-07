# 股票分析终端 - 无GUI版本

## 功能特点

- ✅ 无GUI界面，运行速度快
- ✅ 自动后台运行
- ✅ 生成文本报告
- ✅ Telegram通知
- ✅ 每个交易日早上9:30自动运行

## 文件说明

- `stock_terminal_nogui.py` - 主程序（无GUI版本）
- `run_stock_terminal.sh` - 启动脚本
- `STOCK_TERMINAL_NOGUI_GUIDE.md` - 本说明文档

## 配置步骤

### 1. 配置Telegram

#### 1.1 创建Telegram Bot

1. 在Telegram中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按照提示创建你的bot，会获得一个 **Bot Token**
4. 记下这个Token，格式类似：`123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

#### 1.2 获取Chat ID

1. 在Telegram中搜索 `@userinfobot` 或 `@getidsbot`
2. 发送任意消息给这个bot
3. 它会回复你的 **Chat ID**
4. 记下这个Chat ID，格式类似：`123456789`

#### 1.3 测试Bot

1. 在Telegram中搜索你创建的bot（用bot的用户名）
2. 发送 `/start` 命令
3. 确保bot能正常回复

### 2. 配置脚本

编辑 `run_stock_terminal.sh` 文件，填入你的Telegram配置：

```bash
export TELEGRAM_BOT_TOKEN="你的Telegram Bot Token"
export TELEGRAM_CHAT_ID="你的Telegram Chat ID"
```

### 3. 手动测试

运行脚本测试是否正常：

```bash
/Users/wtueeq/.openclaw/workspace/run_stock_terminal.sh
```

检查：
- 是否收到Telegram通知
- 日志文件是否正常：`~/.stock_terminal/logs/cron.log`
- 报告文件是否生成：`~/.stock_terminal/daily_report.txt`

### 4. 设置定时任务

#### 4.1 编辑crontab

```bash
crontab -e
```

#### 4.2 添加定时任务

添加以下内容（每个交易日早上9:30运行）：

```bash
# 股票分析终端 - 每个交易日早上9:30运行
30 9 * * 1-5 /Users/wtueeq/.openclaw/workspace/run_stock_terminal.sh
```

说明：
- `30 9` - 每天9:30
- `* * 1-5` - 周一到周五（交易日）
- 后面是脚本路径

#### 4.3 保存并退出

- 如果是vim编辑器：按 `Esc`，输入 `:wq`，按 `Enter`
- 如果是nano编辑器：按 `Ctrl+O` 保存，按 `Ctrl+X` 退出

### 5. 验证定时任务

查看定时任务列表：

```bash
crontab -l
```

查看cron日志：

```bash
tail -f ~/.stock_terminal/logs/cron.log
```

## 文件位置

- 主程序：`/Users/wtueeq/.openclaw/workspace/stock_terminal_nogui.py`
- 启动脚本：`/Users/wtueeq/.openclaw/workspace/run_stock_terminal.sh`
- 数据目录：`~/.stock_terminal/`
- 日志文件：`~/.stock_terminal/logs/terminal.log`
- Cron日志：`~/.stock_terminal/logs/cron.log`
- 历史记录：`~/.stock_terminal/history.csv`
- 缓存数据：`~/.stock_terminal/cache.csv`
- 日报文件：`~/.stock_terminal/daily_report.txt`

## 手动运行

如果需要手动运行（不等待定时任务）：

```bash
/Users/wtueeq/.openclaw/workspace/run_stock_terminal.sh
```

或者直接运行Python脚本：

```bash
cd /Users/wtueeq/.openclaw/workspace
python3 stock_terminal_nogui.py
```

## 查看日志

### 查看程序日志

```bash
tail -f ~/.stock_terminal/logs/terminal.log
```

### 查看Cron日志

```bash
tail -f ~/.stock_terminal/logs/cron.log
```

### 查看最新报告

```bash
cat ~/.stock_terminal/daily_report.txt
```

## 停止定时任务

如果需要停止定时任务：

```bash
crontab -e
```

删除或注释掉（在行首加 `#`）股票分析相关的行。

## 故障排除

### 问题1：没有收到Telegram通知

**检查：**
1. Bot Token和Chat ID是否正确
2. 是否在Telegram中给bot发送过 `/start` 命令
3. 查看日志：`~/.stock_terminal/logs/terminal.log`

**解决：**
- 重新获取Bot Token和Chat ID
- 确保bot能正常工作
- 检查网络连接

### 问题2：定时任务没有运行

**检查：**
1. 查看cron日志：`~/.stock_terminal/logs/cron.log`
2. 查看系统cron日志：`/var/log/syslog`（需要sudo权限）

**解决：**
- 确保脚本有执行权限：`chmod +x run_stock_terminal.sh`
- 确保路径正确
- 检查cron服务是否运行：`sudo systemctl status cron`

### 问题3：数据获取失败

**检查：**
1. 查看日志：`~/.stock_terminal/logs/terminal.log`
2. 检查网络连接
3. 检查akshare是否正常安装

**解决：**
- 等待网络恢复
- 重新安装akshare：`pip3 install akshare --upgrade`
- 检查是否有缓存数据可用

## 参数说明

### 买入阈值

默认：88分

可以在 `stock_terminal_nogui.py` 中修改：

```python
BUY_THRESHOLD = 88  # AI评分买入阈值
```

### 市值范围

默认：5亿-20亿

可以在 `_process_stock_data` 函数中修改：

```python
small = df[(df["总市值"] > 5e8) & (df["总市值"] < 2e10)].copy()
```

### 因子权重

默认：
- 动量因子：35%
- 成交量因子：28%
- 换手率因子：22%
- 市值因子：15%

可以在 `stock_terminal_nogui.py` 中修改：

```python
weights = {
    "动量因子": 0.35,
    "成交量因子": 0.28,
    "换手率因子": 0.22,
    "市值因子": 0.15
}
```

## 注意事项

⚠️ **风险提示：**
- 本工具仅提供决策参考，不构成投资建议
- 股市有风险，投资需谨慎
- 请根据自身情况谨慎决策

⚠️ **使用建议：**
- 建议先手动测试，确认正常后再设置定时任务
- 定期检查日志，确保程序正常运行
- 根据市场情况调整参数

## 联系方式

如有问题，请联系小鱼儿 🐟
