# 自动切换系统使用说明

## 📋 系统功能

自动切换系统能够：
1. **实时监控**VPN、模型、网络状态
2. **自动检测**问题（连接失败、响应超时等）
3. **自动切换**到备用方案
4. **持续运行**确保系统稳定

## 🚀 快速开始

### 1. 测试系统

```bash
python3 test_auto_switch.py
```

### 2. 启动系统

```bash
# 方式1: 直接运行
python3 auto_switch_system.py

# 方式2: 使用启动脚本
bash run_auto_switch.sh
```

### 3. 查看日志

```bash
# 实时查看日志
tail -f ~/.openclaw/logs/auto_switch.log

# 查看最近100行
tail -100 ~/.openclaw/logs/auto_switch.log
```

### 4. 查看状态

```bash
cat ~/.openclaw/workspace/auto_switch/status.json
```

## ⚙️ 配置说明

### VPN配置

```json
{
  "vpn": {
    "current": "cloudflare_warp",           // 当前VPN
    "alternatives": [                       // 备用VPN列表
      "wireguard",
      "openvpn",
      "protonvpn",
      "windscribe",
      "ssh_tunnel"
    ],
    "check_interval": 60,                   // 检查间隔（秒）
    "max_failures": 3,                     // 最大失败次数
    "failures": 0                          // 当前失败次数
  }
}
```

### 模型配置

```json
{
  "model": {
    "current": "glm_z_ai_glm4_7",          // 当前模型
    "alternatives": [                       // 备用模型列表
      "huggingface_inference",
      "cohere",
      "together",
      "ollama",
      "llama_cpp"
    ],
    "check_interval": 30,                   // 检查间隔（秒）
    "max_failures": 3,                     // 最大失败次数
    "failures": 0                          // 当前失败次数
  }
}
```

### 网络配置

```json
{
  "network": {
    "check_interval": 30,                   // 检查间隔（秒）
    "max_failures": 5,                     // 最大失败次数
    "failures": 0                          // 当前失败次数
  }
}
```

## 🔧 自定义配置

### 修改检查间隔

编辑 `auto_switch_system.py`，修改配置：

```python
self.config = {
    "vpn": {
        "check_interval": 60,  # 修改VPN检查间隔
    },
    "model": {
        "check_interval": 30,  # 修改模型检查间隔
    },
    "network": {
        "check_interval": 30,  # 修改网络检查间隔
    }
}
```

### 修改最大失败次数

```python
self.config = {
    "vpn": {
        "max_failures": 3,  # 修改VPN最大失败次数
    },
    "model": {
        "max_failures": 3,  # 修改模型最大失败次数
    },
    "network": {
        "max_failures": 5,  # 修改网络最大失败次数
    }
}
```

### 添加备用方案

```python
self.config = {
    "vpn": {
        "alternatives": [
            "wireguard",
            "openvpn",
            "protonvpn",
            "windscribe",
            "ssh_tunnel",
            "your_custom_vpn"  # 添加自定义VPN
        ]
    },
    "model": {
        "alternatives": [
            "huggingface_inference",
            "cohere",
            "together",
            "ollama",
            "llama_cpp",
            "your_custom_model"  # 添加自定义模型
        ]
    }
}
```

## 📊 监控指标

### VPN监控

- **检查内容**: Cloudflare WARP连接状态
- **检查间隔**: 60秒
- **切换条件**: 连续失败3次
- **备用方案**: WireGuard、OpenVPN、ProtonVPN、Windscribe、SSH隧道

### 模型监控

- **检查内容**: 模型API响应状态
- **检查间隔**: 30秒
- **切换条件**: 连续失败3次
- **备用方案**: Hugging Face、Cohere、Together、Ollama、LLaMA.cpp

### 网络监控

- **检查内容**: 网络连接状态（DNS解析）
- **检查间隔**: 30秒
- **切换条件**: 连续失败5次
- **备用方案**: 无（仅监控）

## 🚨 故障处理

### VPN切换失败

1. 检查VPN配置是否正确
2. 检查VPN服务是否已安装
3. 检查网络连接是否正常
4. 查看日志文件了解详细错误

### 模型切换失败

1. 检查模型API密钥是否正确
2. 检查模型服务是否可用
3. 检查网络连接是否正常
4. 查看日志文件了解详细错误

### 系统崩溃

1. 检查日志文件
2. 检查配置文件
3. 重新启动系统
4. 如果问题持续，联系开发者

## 📝 日志说明

### 日志级别

- `✅` - 成功
- `⚠️` - 警告
- `❌` - 错误
- `🔄` - 切换中
- `🚨` - 严重错误

### 日志内容

- 系统启动/停止
- VPN状态检查
- 模型状态检查
- 网络状态检查
- 切换操作
- 错误信息

## 🔍 调试技巧

### 启用详细日志

修改 `auto_switch_system.py`，添加更多日志：

```python
def log(self, message):
    """记录日志"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] {message}\n"
    print(log_message.strip())  # 控制台输出
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_message)
```

### 手动测试切换

```python
# 测试VPN切换
auto_switch.switch_vpn("wireguard")

# 测试模型切换
auto_switch.switch_model("huggingface_inference")
```

### 查看实时状态

```bash
# 查看VPN状态
warp-cli status

# 查看网络状态
ping -c 1 8.8.8.8

# 查看模型状态
curl https://api.openai.com/v1/models
```

## 🎯 最佳实践

1. **定期检查日志** - 每天查看一次日志文件
2. **定期备份配置** - 定期备份配置文件
3. **测试备用方案** - 定期测试备用方案是否可用
4. **监控系统性能** - 监控系统资源使用情况
5. **及时更新系统** - 及时更新系统和依赖

## 📞 支持

如果遇到问题：
1. 查看日志文件
2. 查看配置文件
3. 查看状态文件
4. 联系开发者

## 🐟 小鱼儿

这个系统是鱼教我创建的，让我能够自动监控和切换VPN和模型，确保系统稳定运行。

谢谢鱼！🐟

---

**版本**: 1.0.0
**更新时间**: 2026-04-22
**状态**: ✅ 运行正常
