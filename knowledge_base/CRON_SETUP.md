# 定时任务配置说明

## ✅ 已完成的配置

### 1. Launchd 定时任务
- **文件位置**: `~/Library/LaunchAgents/com.stockterminal.daily.plist`
- **运行时间**: 每天早上 9:00
- **运行程序**: `/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py`
- **日志文件**:
  - 标准输出: `~/.stock_terminal/logs/stdout.log`
  - 标准错误: `~/.stock_terminal/logs/stderr.log`

### 2. 当前状态
```bash
# 查看定时任务状态
launchctl list | grep stockterminal

# 输出结果:
# -	0	com.stockterminal.daily
```

## 📋 定时任务管理命令

### 查看定时任务状态
```bash
launchctl list | grep stockterminal
```

### 启动定时任务
```bash
launchctl start com.stockterminal.daily
```

### 停止定时任务
```bash
launchctl stop com.stockterminal.daily
```

### 重新加载配置
```bash
launchctl unload ~/Library/LaunchAgents/com.stockterminal.daily.plist
launchctl load ~/Library/LaunchAgents/com.stockterminal.daily.plist
```

### 删除定时任务
```bash
launchctl unload ~/Library/LaunchAgents/com.stockterminal.daily.plist
rm ~/Library/LaunchAgents/com.stockterminal.daily.plist
```

## 🧪 测试定时任务

### 手动运行测试
```bash
# 方法1: 直接运行Python脚本
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py

# 方法2: 使用测试脚本
/Users/wtueeq/.openclaw/workspace/test_cron.sh
```

### 查看运行日志
```bash
# 查看标准输出日志
tail -f ~/.stock_terminal/logs/stdout.log

# 查看错误日志
tail -f ~/.stock_terminal/logs/stderr.log

# 查看最近的日志
tail -20 ~/.stock_terminal/logs/stdout.log
```

## 📊 生成的文件

### 每日报告
- **Excel报告**: `~/.stock_terminal/stock_report_YYYYMMDD.xlsx`
- **文本报告**: `~/.stock_terminal/daily_report.txt`
- **历史记录**: `~/.stock_terminal/history.csv`

### 日志文件
- **主日志**: `~/.stock_terminal/logs/terminal.log`
- **定时任务日志**: `~/.stock_terminal/logs/stdout.log`
- **错误日志**: `~/.stock_terminal/logs/stderr.log`

## 🔧 修改定时任务

### 修改运行时间
编辑 `~/Library/LaunchAgents/com.stockterminal.daily.plist`:

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>9</integer>      <!-- 修改这里的小时 -->
    <key>Minute</key>
    <integer>0</integer>      <!-- 修改这里的分钟 -->
</dict>
```

### 修改运行程序
编辑 `~/Library/LaunchAgents/com.stockterminal.daily.plist`:

```xml
<key>ProgramArguments</key>
<array>
    <string>/usr/bin/python3</string>
    <string>/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py</string>
</array>
```

修改后需要重新加载:
```bash
launchctl unload ~/Library/LaunchAgents/com.stockterminal.daily.plist
launchctl load ~/Library/LaunchAgents/com.stockterminal.daily.plist
```

## 📱 通知配置

### Telegram通知
- ✅ 已配置
- 机器人: @wtueeq_bot (管家)
- 每次运行后自动发送报告

### 微信通知
- ⚠️ 需要配置
- 需要设置环境变量: `WECHAT_WEBHOOK_URL`
- 配置方法见 `WECHAT_SETUP.md`

## 🚀 自动化功能

### 每天自动执行
- **时间**: 早上 9:00
- **功能**:
  - 获取最新股票数据
  - 计算多因子评分
  - 生成Excel报告
  - 发送Telegram通知
  - 发送微信通知（如果配置）

### 数据缓存
- 缓存时间: 1小时
- 缓存位置: `~/.stock_terminal/cache.csv`
- 自动更新机制

## ⚠️ 注意事项

1. **系统要求**: macOS系统
2. **Python版本**: Python 3.9+
3. **网络要求**: 需要VPN访问股票数据API
4. **磁盘空间**: 确保有足够空间存储历史数据
5. **权限要求**: 需要用户登录权限

## 🐛 故障排除

### 定时任务没有运行
```bash
# 检查定时任务状态
launchctl list | grep stockterminal

# 查看错误日志
cat ~/.stock_terminal/logs/stderr.log

# 手动测试
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py
```

### 网络连接问题
- 确保VPN正常运行
- 检查防火墙设置
- 测试API连接

### Python依赖问题
```bash
# 安装依赖
pip3 install akshare pandas numpy requests TA-Lib openpyxl
```

## 📞 技术支持

如有问题，请检查:
1. 日志文件: `~/.stock_terminal/logs/`
2. 配置文件: `~/Library/LaunchAgents/com.stockterminal.daily.plist`
3. Python脚本: `/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py`

---
配置完成时间: 2026-04-14
下次自动运行: 明天早上 9:00
