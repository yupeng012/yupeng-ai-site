# OpenClaw 配对指南

## 问题诊断
当前 Gateway 配置为 Token 认证模式，但缺少配对的凭证。

## 解决方案

### 方法 1：通过 Control UI 完成配对（推荐）
1. 打开 Control UI 界面（通常是 http://localhost:18789）
2. 查找配对提示或二维码
3. 使用移动设备扫描二维码或输入配对码
4. 配对完成后，Gateway 会自动重启

### 方法 2：重新运行 Onboard
如果 Control UI 无法访问，可以重新运行 onboarding 流程：
```bash
openclaw onboard
```
这会引导你完成整个设置流程，包括配对。

### 方法 3：临时禁用认证（仅限本地测试）
**警告：仅在内网/本地环境使用！**

编辑 `~/.openclaw/openclaw.json`，修改：
```json
{
  "gateway": {
    "auth": {
      "mode": "none"  // 临时禁用认证
    }
  }
}
```
然后重启 Gateway：
```bash
openclaw gateway restart
```

## 配对后
配对完成后，你可以：
- 正常使用所有 CLI 命令
- 安装和使用技能（如 find-skill, tavily-search）
- 配置 Telegram 等渠道
- 使用所有工具和功能

## 常见问题
- **配对码无效**：确保设备在同一网络
- **二维码不显示**：检查 Control UI 是否正确加载
- **配对后仍然报错**：尝试重启 Gateway

## 下一步
完成配对后，你可以：
1. 安装 Telegram 渠道
2. 配置 Tavily Search
3. 使用其他技能
