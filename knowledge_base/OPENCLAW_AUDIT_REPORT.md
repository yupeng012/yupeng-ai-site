# OpenClaw 系统检测报告

## 📊 检测概览

**检测时间**: 2026-04-19 10:10  
**系统版本**: 2026.3.12  
**最新版本**: 2026.4.15  
**配置版本**: 2026.4.14  
**操作系统**: macOS 26.4.1 (arm64)  
**Node版本**: 24.14.0

---

## ⚠️ 关键问题

### 1. 版本不匹配 🔴

**问题描述**:
- 当前运行版本: 2026.3.12
- 配置文件版本: 2026.4.14
- 最新可用版本: 2026.4.15

**影响**:
- 配置文件由新版本写入，但旧版本运行可能导致兼容性问题
- 缺少新版本的功能和修复

**解决方案**:
```bash
# 更新到最新版本
npm install -g openclaw@2026.4.15

# 或使用本地安装
npm install -g --prefix /Users/wtueeq/.local openclaw@2026.4.15
```

### 2. 插件冲突 🔴

**问题描述**:
- memory-core插件重复ID检测到
- memory-core插件注册失败
- 错误: `TypeError: register.registerMemoryEmbeddingProvider is not a function`

**影响**:
- 内存搜索功能可能无法正常工作
- 语义搜索功能不可用

**解决方案**:
```bash
# 运行修复命令
openclaw doctor --fix

# 或手动清理重复插件
rm -rf /usr/local/lib/node_modules/openclaw/extensions/memory-core
```

### 3. 安全配置问题 🔴

**问题描述**:
- Telegram群组策略设置为"open"
- 存在3个严重安全问题
- 工具权限过于开放

**影响**:
- 任何Telegram群组都可以添加机器人
- 存在提示注入攻击风险
- 文件系统和运行时工具暴露

**解决方案**:
```bash
# 修改配置文件
openclaw config set channels.telegram.groupPolicy allowlist

# 或手动编辑配置文件
# 编辑 ~/.openclaw/openclaw.json
# 将 "groupPolicy": "open" 改为 "groupPolicy": "allowlist"
```

---

## ⚡ 警告问题

### 1. 反向代理配置 ⚠️

**问题描述**:
- `gateway.trustedProxies` 为空
- 如果通过反向代理暴露Control UI，存在安全风险

**解决方案**:
```bash
# 如果使用反向代理，配置信任的代理IP
openclaw config set gateway.trustedProxies "your_proxy_ip"

# 或保持Control UI仅本地访问
```

### 2. 不安全的认证配置 ⚠️

**问题描述**:
- `gateway.controlUi.allowInsecureAuth=true` 已启用
- 存在不安全的认证配置

**解决方案**:
```bash
# 禁用不安全的认证
openclaw config set gateway.controlUi.allowInsecureAuth false

# 或使用HTTPS/Tailscale Serve
```

### 3. 多用户环境检测 ⚠️

**问题描述**:
- 检测到潜在的多用户设置
- 个人助手模型警告

**解决方案**:
- 如果是多用户环境，建议分离信任边界
- 设置适当的沙箱模式
- 限制工具权限

### 4. 插件安装未固定版本 ⚠️

**问题描述**:
- openclaw-weixin插件使用未固定的npm规格

**解决方案**:
```bash
# 固定插件版本
# 编辑配置文件，将版本号固定为具体版本
```

---

## 📈 系统状态

### ✅ 正常运行

**Gateway服务**:
- 状态: 运行中
- PID: 32231
- 绑定: 127.0.0.1:18789
- 认证: token认证

**通道状态**:
- Telegram: ✅ 正常
- 微信: ⚠️ 需要配置token

**Agent状态**:
- main: ✅ 活跃
- stock-analyst: ✅ 活跃
- 会话数: 12个活跃会话

**内存状态**:
- 文件数: 3个
- 数据块: 30个
- 状态: dirty
- FTS: 就绪

### ⚠️ 需要关注

**插件状态**:
- 已加载: 2个
- 已禁用: 40个
- 错误: 1个 (memory-core)

**技能状态**:
- 符合条件: 17个
- 缺少依赖: 45个
- 被阻止: 0个

**内存搜索**:
- 状态: 已启用但未配置embedding provider
- 影响: 语义搜索无法工作

---

## 🔧 推荐操作

### 立即执行（高优先级）

1. **更新OpenClaw版本**
   ```bash
   npm install -g --prefix /Users/wtueeq/.local openclaw@2026.4.15
   ```

2. **修复插件问题**
   ```bash
   openclaw doctor --fix
   ```

3. **修复安全配置**
   ```bash
   openclaw config set channels.telegram.groupPolicy allowlist
   openclaw config set gateway.controlUi.allowInsecureAuth false
   ```

### 建议执行（中优先级）

1. **配置内存搜索**
   ```bash
   # 配置embedding provider
   openclaw config set agents.defaults.memorySearch.provider "openai"
   # 或设置本地模型
   ```

2. **清理重复服务**
   ```bash
   # 检测到多个gateway-like服务
   # 建议只保留一个
   ```

3. **固定插件版本**
   ```bash
   # 固定openclaw-weixin版本
   ```

### 可选执行（低优先级）

1. **配置反向代理**
   ```bash
   # 如果需要，配置trusted proxies
   ```

2. **优化技能依赖**
   ```bash
   # 安装缺失的技能依赖
   ```

---

## 📊 详细问题列表

### 严重问题 (3个)

1. **Open groupPolicy with elevated tools enabled**
   - 位置: channels.telegram.groupPolicy
   - 风险: 提示注入攻击
   - 修复: 设置为allowlist

2. **Open groupPolicy with runtime/filesystem tools exposed**
   - 位置: agents.defaults, agents.list.main, agents.list.stock-analyst
   - 风险: 文件系统和运行时工具暴露
   - 修复: 限制工具权限

3. **Telegram security warning**
   - 位置: channels.telegram.groupPolicy
   - 风险: 任何群组都可以添加
   - 修复: 配置groups allowlist

### 警告问题 (5个)

1. **Reverse proxy headers are not trusted**
   - 位置: gateway.trustedProxies
   - 风险: 反向代理安全风险
   - 修复: 配置trusted proxies

2. **Control UI insecure auth toggle enabled**
   - 位置: gateway.controlUi.allowInsecureAuth
   - 风险: 不安全的认证
   - 修复: 禁用或使用HTTPS

3. **Insecure or dangerous config flags enabled**
   - 位置: gateway.controlUi.allowInsecureAuth
   - 风险: 不安全配置
   - 修复: 禁用不安全标志

4. **Potential multi-user setup detected**
   - 位置: channels.telegram.groupPolicy
   - 风险: 多用户环境安全风险
   - 修复: 分离信任边界

5. **Plugin installs include unpinned npm specs**
   - 位置: openclaw-weixin
   - 风险: 供应链稳定性
   - 修复: 固定版本号

### 信息问题 (1个)

1. **Attack surface summary**
   - 群组: open=1, allowlist=0
   - 工具: elevated=enabled
   - 信任模型: personal assistant

---

## 🎯 修复优先级

### 🔴 立即修复（今天）

1. 更新OpenClaw到最新版本
2. 修复memory-core插件问题
3. 修改Telegram群组策略为allowlist

### 🟡 尽快修复（本周）

1. 禁用不安全的认证配置
2. 配置内存搜索embedding provider
3. 清理重复的gateway服务

### 🟢 计划修复（本月）

1. 固定插件版本
2. 优化技能依赖
3. 配置反向代理（如需要）

---

## 📝 修复脚本

### 自动修复脚本

```bash
#!/bin/bash
# OpenClaw 自动修复脚本

echo "🔧 开始修复OpenClaw..."

# 1. 更新版本
echo "📦 更新OpenClaw版本..."
npm install -g --prefix /Users/wtueeq/.local openclaw@2026.4.15

# 2. 修复配置
echo "⚙️  修复配置..."
openclaw config set channels.telegram.groupPolicy allowlist
openclaw config set gateway.controlUi.allowInsecureAuth false

# 3. 运行doctor
echo "🏥 运行doctor..."
openclaw doctor --fix

# 4. 重启gateway
echo "🔄 重启gateway..."
openclaw gateway restart

echo "✅ 修复完成！"
```

### 手动修复步骤

1. **更新版本**
   ```bash
   npm install -g --prefix /Users/wtueeq/.local openclaw@2026.4.15
   ```

2. **修复配置**
   ```bash
   openclaw config set channels.telegram.groupPolicy allowlist
   openclaw config set gateway.controlUi.allowInsecureAuth false
   ```

3. **运行修复**
   ```bash
   openclaw doctor --fix
   ```

4. **重启服务**
   ```bash
   openclaw gateway restart
   ```

---

## 📞 获取帮助

如果遇到问题：

1. **查看文档**: https://docs.openclaw.ai
2. **运行诊断**: `openclaw doctor`
3. **查看日志**: `openclaw logs --follow`
4. **安全审计**: `openclaw security audit --deep`

---

## 🎉 总结

**系统状态**: ⚠️ 需要修复  
**严重问题**: 3个  
**警告问题**: 5个  
**信息问题**: 1个  

**建议**: 立即执行高优先级修复，确保系统安全和稳定运行。

---

**报告生成时间**: 2026-04-19 10:10  
**检测工具**: openclaw doctor, openclaw security audit  
**系统版本**: OpenClaw 2026.3.12
