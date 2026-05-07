# 🚀 NVIDIA API快速配置

## 一键配置

```bash
cd ~/.openclaw/workspace
python3 set_nvidia_key.py <your_api_key>
```

## 可用的免费模型

| 模型 | 参数 | 上下文 | 特性 |
|------|------|--------|------|
| Llama 3.1 405B Instruct ⭐ | 405B | 131K | 最强推理 |
| Llama 3.1 70B Instruct | 70B | 131K | 高性能 |
| Llama 3.1 8B Instruct | 8B | 131K | 快速响应 |
| Mistral Large | 大型 | 32K | 多语言 |
| Mixtral 8x7B Instruct | 8x7B | 32K | MoE架构 |

## 推荐配置

### 最强性能（推荐）
```bash
python3 configure_nvidia.py
# 选择选项4
```

### 性价比高
```bash
python3 configure_nvidia.py
# 选择选项5
```

### 快速响应
```bash
python3 configure_nvidia.py
# 选择选项6
```

## 验证配置

```bash
cd ~/.openclaw/workspace
python3 configure_nvidia.py
# 选择选项9测试NVIDIA连接
```

## 详细文档

- 📖 [完整配置指南](./NVIDIA_CONFIG_GUIDE.md)
- 📖 [API Keys配置指南](./API_KEYS_GUIDE.md)

## 在代码中使用

```python
import json
from pathlib import Path
import requests

# 读取配置
config_file = Path.home() / ".openclaw" / "workspace" / "api_keys.json"
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取NVIDIA配置
api_key = config['nvidia']['api_key']
model = config['nvidia']['default_model']
base_url = config['nvidia']['base_url']

# 使用NVIDIA API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(
    f"{base_url}/chat/completions",
    headers=headers,
    json={
        "model": model,
        "messages": [{"role": "user", "content": "你好！"}]
    }
)

print(response.json())
```

## 模型特性

### Llama 3.1系列
- ✅ 131K超长上下文
- ✅ 强大的推理能力
- ✅ 优秀的性能
- ✅ 完全免费

### Mistral系列
- ✅ 优秀的多语言能力
- ✅ MoE架构高效
- ✅ 快速响应

## 获取API Key

1. 访问 https://build.nvidia.com/
2. 登录或注册账号
3. 创建API Key
4. 复制API Key（格式：`nvapi-xxxxxxxxxxxxx`）

---

**小鱼儿 🐟** | 2026-04-24
