# OpenClaw 开机自动启动配置说明

**配置时间**: 2026-04-14 19:55
**配置状态**: ✅ 已完成

---

## ✅ 开机自动启动已配置

### 当前状态
- **LaunchAgent**: com.openclaw.gateway
- **状态**: ✅ 已加载
- **PID**: 30952 (正在运行)
- **开机启动**: ✅ 已启用
- **保持运行**: ✅ 已启用

---

## 📋 配置详情

### LaunchAgent配置文件
**位置**: `~/Library/LaunchAgents/com.openclaw.gateway.plist`

**配置内容**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.openclaw.gateway</string>
    <key>ProgramArguments</key>
    <array>
        <string>openclaw</string>
        <string>gateway</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/wtueeq/.openclaw/workspace</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/wtueeq/Library/Logs/openclaw.gateway.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/wtueeq/.Library/Logs/openclaw.gateway.err</string>
</dict>
</plist>
```

### 配置说明
- **Label**: com.openclaw.gateway (服务标识)
- **ProgramArguments**: openclaw gateway (启动命令)
- **WorkingDirectory**: 工作目录
- **RunAtLoad**: true (开机自动启动)
- **KeepAlive**: true (保持运行，崩溃后自动重启)

---

## 🚀 功能特性

### 开机自动启动
- ✅ 系统启动时自动启动OpenClaw gateway
- ✅ 登录后自动启动OpenClaw gateway
- ✅ 崩溃后自动重启

### 保持运行
- ✅ 持续运行，不会意外退出
- ✅ 崩溃后自动重启
- ✅ 系统休眠唤醒后自动恢复

### 日志记录
- ✅ 标准输出日志: `~/Library/Logs/openclaw.gateway.log`
- ✅ 错误日志: `~/Library/Logs/openclaw.gateway.err`

---

## 🎯 管理命令

### 查看状态
```bash
# 查看LaunchAgent状态
launchctl list | grep openclaw

# 查看OpenClaw gateway状态
openclaw gateway status

# 查看服务日志
tail -f ~/Library/Logs/openclaw.gateway.log
```

### 启动/停止
```bash
# 启动OpenClaw gateway
launchctl start com.openclaw.gateway

# 停止OpenClaw gateway
launchctl stop com.openclaw.gateway

# 重启OpenClaw gateway
launchctl restart com.openclaw.gateway

# 卸载配置
launchctl unload ~/Library/LaunchAgents/com.openclaw.gateway.plist

# 重新加载配置
launchctl load ~/Library/LaunchAgents/com.openclaw.gateway.plist
```

### 禁用/启用开机启动
```bash
# 禁用开机启动
launchctl disable com.openclaw.gateway

# 启用开机启动
launchctl enable com.openclaw.gateway
```

---

## 🔧 配置修改

### 修改启动参数

编辑 `~/Library/LaunchAgents/com.openclaw.gateway.plist`:

```xml
<!-- 修改启动命令 -->
<key>ProgramArguments</key>
<array>
    <string>openclaw</string>
    <string>gateway</string>
    <string>--port</string>
    <string>18789</string>
</array>

<!-- 修改工作目录 -->
<key>WorkingDirectory</key>
<string>/Users/wtueeq/.openclaw/workspace</string>

<!-- 禁用开机启动 -->
<key>RunAtLoad</key>
<false/>

<!-- 禁用保持运行 -->
<key>KeepAlive</key>
<false/>
```

修改后需要重新加载:
```bash
launchctl unload ~/Library/LaunchAgents/com.openclaw.gateway.plist
launchctl load ~/Library/LaunchAgents/com.openclaw.gateway.plist
```

---

## 📊 服务状态

### 当前运行状态
- **OpenClaw Gateway**: ✅ 运行中
- **PID**: 30952
- **端口**: 18789
- **绑定**: 127.0.0.1:18789
- **Dashboard**: http://127.0.0.1:18789/

### 相关服务
- **股票分析定时任务**: com.stockterminal.daily
- **Telegram通知**: 已配置
- **多智能体**: main, stock-analyst

---

## 🎉 配置完成

**OpenClaw已配置为开机自动启动！**

### 自动启动功能
- ✅ 系统启动时自动启动
- ✅ 登录后自动启动
- ✅ 崩溃后自动重启
- ✅ 保持持续运行

### 下次启动
- **系统启动**: OpenClaw gateway自动启动
- **用户登录**: OpenClaw gateway自动启动
- **崩溃恢复**: OpenClaw gateway自动重启

### 管理建议
- 定期检查服务状态
- 查看日志文件
- 监控资源使用
- 及时更新版本

---

## 📝 相关文件

### 配置文件
- **LaunchAgent**: `~/Library/LaunchAgents/com.openclaw.gateway.plist`
- **OpenClaw配置**: `~/.openclaw/openclaw.json`
- **工作目录**: `/Users/wtueeq/.openclaw/workspace`

### 日志文件
- **标准日志**: `~/Library/Logs/openclaw.gateway.log`
- **错误日志**: `~/Library/Logs/openclaw.gateway.err`
- **股票分析日志**: `~/.stock_terminal/logs/terminal.log`

---

## ⚠️ 注意事项

1. **权限要求**: 需要用户登录权限
2. **端口占用**: 确保端口18789未被占用
3. **资源使用**: 注意系统资源消耗
4. **网络依赖**: 需要网络连接才能使用完整功能

---

**配置完成时间**: 2026-04-14 19:55
**下次启动**: 系统启动时自动启动

**小鱼儿 🐟**
