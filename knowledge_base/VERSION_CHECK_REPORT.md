# OpenClaw 版本检测报告

## 📊 版本状态

### 当前系统版本
- **命令**: `openclaw --version`
- **结果**: OpenClaw 2026.3.12 (6472949)
- **路径**: `/usr/local/bin/openclaw`

### 已安装的新版本
- **命令**: `/Users/wtueeq/.local/bin/openclaw --version`
- **结果**: OpenClaw 2026.4.15 (041266a)
- **路径**: `/Users/wtueeq/.local/bin/openclaw`

## 🔍 问题分析

### PATH 优先级问题
```
/usr/local/bin              # 旧版本 (2026.3.12) - 优先级高
/Users/wtueeq/.local/bin    # 新版本 (2026.4.15) - 优先级低
```

### 文件权限
- `/usr/local/bin/openclaw` 属于 root 用户
- 需要sudo权限才能修改
- 符号链接指向: `/usr/local/lib/node_modules/openclaw/openclaw.mjs`

## 💡 解决方案

### 方案1: 创建别名（推荐，无需sudo）

在 `~/.zshrc` 中添加别名：

```bash
# OpenClaw 别名 - 使用新版本
alias openclaw='/Users/wtueeq/.local/bin/openclaw'
```

然后重新加载配置：
```bash
source ~/.zshrc
```

### 方案2: 调整PATH顺序

修改 `~/.zshrc`，将 `/Users/wtueeq/.local/bin` 放在最前面：

```bash
export PATH="/Users/wtueeq/.local/bin:$PATH"
```

### 方案3: 使用完整路径

每次使用时指定完整路径：
```bash
/Users/wtueeq/.local/bin/openclaw status
```

### 方案4: 替换系统版本（需要sudo）

```bash
# 删除旧版本符号链接
sudo rm /usr/local/bin/openclaw

# 创建新版本符号链接
sudo ln -s /Users/wtueeq/.local/lib/node_modules/openclaw/openclaw.mjs /usr/local/bin/openclaw
```

## 🎯 推荐操作

**立即生效（无需重启终端）**：
```bash
# 添加别名
echo "alias openclaw='/Users/wtueeq/.local/bin/openclaw'" >> ~/.zshrc

# 重新加载配置
source ~/.zshrc

# 验证版本
openclaw --version
# 应该显示: OpenClaw 2026.4.15
```

## 📝 版本对比

| 版本 | 安装位置 | 状态 |
|------|----------|------|
| 2026.3.12 | `/usr/local/lib/node_modules/openclaw` | 旧版本，系统默认 |
| 2026.4.15 | `/Users/wtueeq/.local/lib/node_modules/openclaw` | 新版本，已安装 |

## ⚠️ 注意事项

1. **别名方案**最简单，无需sudo权限
2. **PATH调整**会影响所有命令，需要谨慎
3. **替换系统版本**需要sudo权限，可能影响其他用户
4. **完整路径**最安全，但使用不便

## 🚀 下一步

选择一个方案后，运行验证命令：
```bash
openclaw --version
openclaw status
```

应该不再显示版本不匹配警告。

---

**报告生成时间**: 2026-04-19 08:43
**检测状态**: ✅ 完成
**建议操作**: 使用别名方案
