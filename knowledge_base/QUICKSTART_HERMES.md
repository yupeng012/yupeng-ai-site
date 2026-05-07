# 🚀 Hermes模型快速配置

## 一键配置

```bash
cd ~/.openclaw/workspace
python3 set_hermes_model.py <model_key>
```

## 可用的模型

| 模型 | 参数 | 上下文 | 定价 | 特性 |
|------|------|--------|------|------|
| Hermes 4 70B | 70B | 131K | 低 | 混合推理 |
| Hermes 4 405B | 405B | 131K | 高 | 最强性能 |
| Hermes 3 70B | 70B | 131K | 中 | 代理能力 |
| Hermes 3 405B (免费) ⭐ | 405B | 131K | 免费 | 高性能 |
| Hermes 3 405B | 405B | 131K | 中 | 最强性能 |
| Hermes 2 Pro 8B | 8B | 8K | 低 | 快速响应 |

## 推荐配置

### 免费使用（推荐）
```bash
python3 set_hermes_model.py hermes-3-405b-free
```

### 性价比高
```bash
python3 set_hermes_model.py hermes-3-70b
```

### 最强性能
```bash
python3 set_hermes_model.py hermes-4-405b
```

### 快速响应
```bash
python3 set_hermes_model.py hermes-2-pro-8b
```

## 验证配置

```bash
cd ~/.openclaw/workspace
python3 configure_hermes.py
# 选择选项9测试当前Hermes模型
```

## 详细文档

- 📖 [完整配置指南](./HERMES_CONFIG_GUIDE.md)
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

# 获取Hermes配置
api_key = config['openrouter']['api_key']
model = config['openrouter']['default_model']

# 使用Hermes模型
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": model,
        "messages": [{"role": "user", "content": "你好！"}]
    }
)

print(response.json())
```

## 模型特性

### Hermes 4系列
- ✅ 混合推理能力
- ✅ 131K超长上下文
- ✅ 最强性能

### Hermes 3系列
- ✅ 优秀的代理能力
- ✅ 角色扮演能力
- ✅ 推理能力强
- ✅ 免费版本可用

### Hermes 2 Pro
- ✅ 轻量级
- ✅ 快速响应
- ✅ 性价比高

---

**小鱼儿 🐟** | 2026-04-24
