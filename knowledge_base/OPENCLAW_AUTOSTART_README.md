# 🐟 OpenClaw自动启动和自修复系统

## 📊 系统功能

### ✅ 主要功能

1. **开机自动启动**
   - 系统启动时自动启动OpenClaw
   - 支持macOS、Linux、Windows

2. **后台常驻运行**
   - 持续监控OpenClaw运行状态
   - 自动检测异常情况

3. **自动修复**
   - 检测到OpenClaw停止时自动重启
   - 自动修复配置文件和目录
   - 自动清理日志文件

4. **健康检查**
   - 定期检查OpenClaw健康状态
   - 检查HTTP健康检查接口
   - 检查进程运行状态

5. **日志记录**
   - 记录所有操作和错误
   - 便于问题排查和监控

## 🚀 快速开始

### 1. 启动系统

```bash
cd ~/.openclaw/workspace
./start_openclaw_autostart.sh
```

### 2. 停止系统

```bash
cd ~/.openclaw/workspace
./stop_openclaw_autostart.sh
```

### 3. 检查状态

```bash
cd ~/.openclaw/workspace
./check_openclaw_autostart.sh
```

### 4. 查看日志

```bash
tail -f ~/.openclaw_autostart/autostart.log
```

## ⚙️ 配置说明

### 配置文件位置

```
~/.openclaw_autostart/config.json
```

### 配置参数

```json
{
  "enabled": true,                    // 是否启用
  "check_interval": 60,               // 检查间隔（秒）
  "max_restart_attempts": 5,         // 最大重启尝试次数
  "log_file": "~/.openclaw_autostart/autostart.log",
  "pid_file": "~/.openclaw_autostart/openclaw.pid",
  "health_check_url": "http://localhost:8080/health",
  "auto_repair": true,               // 是否自动修复
  "notification_enabled": true        // 是否启用通知
}
```

## 🔧 系统架构

### 核心组件

1. **OpenClawAutoStarter类**
   - 负责自动启动和自修复逻辑
   - 监控OpenClaw运行状态
   - 执行健康检查和自动修复

2. **启动脚本**
   - `start_openclaw_autostart.sh`
   - 启动自动启动和自修复系统

3. **停止脚本**
   - `stop_openclaw_autostart.sh`
   - 停止自动启动和自修复系统

4. **状态检查脚本**
   - `check_openclaw_autostart.sh`
   - 检查系统运行状态

### 工作流程

```
1. 系统启动
   ↓
2. 检查OpenClaw是否运行
   ↓
3. 如果未运行，启动OpenClaw
   ↓
4. 进入监控循环
   ↓
5. 定期执行健康检查
   ↓
6. 如果检查失败，自动修复
   ↓
7. 如果修复失败，重启OpenClaw
   ↓
8. 继续监控
```

## 🛠️ 故障排查

### 问题1：系统无法启动

**解决方案**：
1. 检查Python是否安装：`python3 --version`
2. 检查OpenClaw是否安装：`openclaw --version`
3. 查看日志文件：`tail -f ~/.openclaw_autostart/autostart.log`

### 问题2：OpenClaw频繁重启

**解决方案**：
1. 检查OpenClaw日志：`openclaw logs`
2. 检查系统资源：`top` 或 `htop`
3. 增加重启间隔：修改配置文件中的`check_interval`

### 问题3：自动修复失败

**解决方案**：
1. 检查配置文件：`cat ~/.openclaw_autostart/config.json`
2. 检查日志文件：`tail -f ~/.openclaw_autostart/autostart.log`
3. 手动修复：删除配置文件，让系统重新创建

## 📊 监控指标

### 关键指标

1. **运行状态**
   - OpenClaw是否运行
   - 自动启动系统是否运行

2. **健康检查**
   - HTTP健康检查状态
   - 进程运行状态

3. **重启次数**
   - 总重启次数
   - 最近重启时间

4. **错误日志**
   - 最近错误信息
   - 错误发生时间

### 监控命令

```bash
# 查看进程
ps aux | grep openclaw

# 查看日志
tail -f ~/.openclaw_autostart/autostart.log

# 查看配置
cat ~/.openclaw_autostart/config.json

# 检查状态
./check_openclaw_autostart.sh
```

## 🎯 最佳实践

### 1. 定期检查

建议每天检查一次系统状态：

```bash
./check_openclaw_autostart.sh
```

### 2. 日志管理

定期清理日志文件，避免占用过多磁盘空间：

```bash
# 清理7天前的日志
find ~/.openclaw_autostart -name "*.log" -mtime +7 -delete
```

### 3. 配置优化

根据实际情况调整配置参数：

```json
{
  "check_interval": 120,              // 增加检查间隔
  "max_restart_attempts": 3,         // 减少重启尝试次数
  "auto_repair": true                // 保持自动修复启用
}
```

### 4. 监控告警

建议配置监控告警，及时发现异常：

```bash
# 创建监控脚本
cat > monitor.sh << 'EOF'
#!/bin/bash
if ! pgrep -f openclaw_autostart.py > /dev/null; then
    echo "OpenClaw自动启动系统未运行！" | mail -s "告警" your@email.com
fi
EOF

# 添加到crontab
crontab -e
# 添加以下行
*/10 * * * * /path/to/monitor.sh
```

## 📚 参考资料

- [OpenClaw文档](https://docs.openclaw.ai)
- [Python文档](https://docs.python.org/3/)
- [系统管理最佳实践](https://www.linux.org/docs/)

---

**🐟 OpenClaw自动启动和自修复系统**

**🚀 让OpenClaw始终保持运行状态！**
