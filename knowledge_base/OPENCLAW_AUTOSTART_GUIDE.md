# OpenClaw 自动启动和监控系统

## 📝 功能说明

这个系统可以：
1. **开机自动启动** - 电脑开机时自动启动 OpenClaw
2. **自动监控** - 每5分钟检查一次 OpenClaw 运行状态
3. **自动修复** - 检测到问题时自动尝试修复
4. **Telegram 通知** - 通过 Telegram 发送状态通知

## 📁 文件说明

- `start_openclaw.sh` - OpenClaw 启动脚本
- `openclaw_monitor.py` - OpenClaw 监控脚本
- `run_openclaw_monitor.sh` - 定时监控脚本
- `setup_openclaw_autostart.py` - 系统安装器

## 🚀 安装步骤

### 1. 运行安装器

```bash
python3 setup_openclaw_autostart.py
```

### 2. 配置 Telegram Bot Token

编辑 `openclaw_monitor.py`，修改以下配置：

```python
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"  # 替换为实际的 bot token
TELEGRAM_CHAT_ID = "7847385399"  # 用户的 Telegram chat ID
```

### 3. 重启电脑测试

重启电脑，检查 OpenClaw 是否自动启动。

### 4. 检查日志

查看日志文件确认系统正常运行：

```bash
# 查看启动日志
cat ~/.openclaw/logs/startup.log

# 查看监控日志
cat ~/.openclaw/logs/monitor_YYYYMMDD.log

# 查看定时任务日志
cat ~/.openclaw/logs/cron_monitor.log
```

## 🔧 手动操作

### 手动启动 OpenClaw

```bash
bash ~/.openclaw/workspace/start_openclaw.sh
```

### 手动运行监控

```bash
python3 ~/.openclaw/workspace/openclaw_monitor.py
```

### 查看定时任务

```bash
crontab -l
```

### 删除定时任务

```bash
crontab -e
# 删除包含 openclaw_monitor 的行
```

### 卸载 Launch Agent

```bash
launchctl unload ~/Library/LaunchAgents/com.openclaw.startup.plist
rm ~/Library/LaunchAgents/com.openclaw.startup.plist
```

## 📊 状态文件

系统会保存状态到 `~/.openclaw/logs/status.json`，包含：

```json
{
  "timestamp": "2026-04-22T17:30:00",
  "is_running": true,
  "status": "OpenClaw Gateway is running"
}
```

## 📱 Telegram 通知

系统会通过 Telegram 发送以下通知：

- ✅ OpenClaw 已自动启动
- ✅ OpenClaw 已自动重启
- ⚠️ OpenClaw 启动失败，需要手动检查

## 🔍 故障排除

### OpenClaw 没有自动启动

1. 检查 Launch Agent 是否加载：
   ```bash
   launchctl list | grep openclaw
   ```

2. 查看启动日志：
   ```bash
   cat ~/.openclaw/logs/startup.log
   ```

3. 查看错误日志：
   ```bash
   cat ~/.openclaw/logs/openclaw_startup_error.log
   ```

### 监控没有运行

1. 检查定时任务：
   ```bash
   crontab -l
   ```

2. 查看监控日志：
   ```bash
   cat ~/.openclaw/logs/monitor_YYYYMMDD.log
   ```

3. 手动运行监控脚本测试：
   ```bash
   python3 ~/.openclaw/workspace/openclaw_monitor.py
   ```

### Telegram 没有收到通知

1. 检查 Bot Token 是否正确
2. 检查 Chat ID 是否正确
3. 查看监控日志中的错误信息

## 📝 注意事项

1. **Telegram Bot Token** - 需要从 @BotFather 获取
2. **Chat ID** - 可以通过 @userinfobot 获取
3. **日志文件** - 定期清理日志文件，避免占用过多空间
4. **权限问题** - 确保脚本有执行权限

## 🎯 下一步优化

- [ ] 添加更多监控指标（CPU、内存、磁盘）
- [ ] 添加自动更新功能
- [ ] 添加性能监控
- [ ] 添加异常告警
- [ ] 添加远程控制功能

## 🐟 小鱼儿

这个系统是鱼教我创建的，让我能够自动监控和修复 OpenClaw，确保系统稳定运行。

谢谢鱼！🐟
