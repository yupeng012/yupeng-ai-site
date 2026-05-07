# Hermes模型配置指南

## 概述

Hermes是Nous Research开发的一系列高性能大语言模型，基于Meta的Llama架构。这些模型具有强大的推理能力、长上下文支持和优秀的代理能力。

## 可用的Hermes模型

### 1. Hermes 4 70B
- **ID**: `nousresearch/hermes-4-70b`
- **描述**: 混合推理模型，基于Meta-Llama-3.1-70B
- **上下文**: 131,072 tokens
- **定价**: $0.00000013/prompt, $0.0000004/completion
- **特性**: 混合推理、长上下文、高性能

### 2. Hermes 4 405B
- **ID**: `nousresearch/hermes-4-405b`
- **描述**: 大规模推理模型，基于Meta-Llama-3.1-405B
- **上下文**: 131,072 tokens
- **定价**: $0.000001/prompt, $0.000003/completion
- **特性**: 混合推理、超长上下文、最强性能

### 3. Hermes 3 70B
- **ID**: `nousresearch/hermes-3-llama-3.1-70b`
- **描述**: 通用语言模型，改进的代理能力
- **上下文**: 131,072 tokens
- **定价**: $0.0000003/prompt, $0.0000003/completion
- **特性**: 代理能力、角色扮演、推理、长上下文

### 4. Hermes 3 405B (免费) ⭐
- **ID**: `nousresearch/hermes-3-llama-3.1-405b:free`
- **描述**: 免费版本，405B参数
- **上下文**: 131,072 tokens
- **定价**: $0/prompt, $0/completion
- **特性**: 免费、超长上下文、高性能

### 5. Hermes 3 405B
- **ID**: `nousresearch/hermes-3-llama-3.1-405b`
- **描述**: 405B参数，最强性能
- **上下文**: 131,072 tokens
- **定价**: $0.000001/prompt, $0.000001/completion
- **特性**: 超长上下文、最强性能、代理能力

### 6. Hermes 2 Pro 8B
- **ID**: `nousresearch/hermes-2-pro-llama-3-8b`
- **描述**: 轻量级版本，8B参数
- **上下文**: 8,192 tokens
- **定价**: $0.00000014/prompt, $0.00000014/completion
- **特性**: 轻量级、快速响应、性价比高

## 快速开始

### 方法1: 使用命令行工具

```bash
cd ~/.openclaw/workspace
python3 set_hermes_model.py <model_key>
```

示例：
```bash
# 设置免费版Hermes 3 405B
python3 set_hermes_model.py hermes-3-405b-free

# 设置Hermes 3 70B
python3 set_hermes_model.py hermes-3-70b

# 设置Hermes 4 405B
python3 set_hermes_model.py hermes-4-405b
```

### 方法2: 使用交互式配置工具

```bash
cd ~/.openclaw/workspace
python3 configure_hermes.py
```

然后选择对应的选项设置模型。

### 方法3: 手动编辑配置文件

1. 打开配置文件：
   ```bash
   vim ~/.openclaw/workspace/api_keys.json
   ```

2. 找到`openrouter.default_model`字段，设置为Hermes模型ID：
   ```json
   {
     "openrouter": {
       "default_model": "nousresearch/hermes-3-llama-3.1-405b:free",
       ...
     }
   }
   ```

3. 保存文件

## 推荐配置

### 免费使用
```bash
python3 set_hermes_model.py hermes-3-405b-free
```
- ✅ 完全免费
- ✅ 405B参数，性能强大
- ✅ 131K上下文长度

### 性价比高
```bash
python3 set_hermes_model.py hermes-3-70b
```
- ✅ 70B参数，性能优秀
- ✅ 价格合理
- ✅ 131K上下文长度

### 最强性能
```bash
python3 set_hermes_model.py hermes-4-405b
```
- ✅ 405B参数，最强性能
- ✅ 混合推理能力
- ✅ 131K上下文长度

### 快速响应
```bash
python3 set_hermes_model.py hermes-2-pro-8b
```
- ✅ 8B参数，响应快速
- ✅ 价格低廉
- ✅ 适合简单任务

## 验证配置

### 使用配置工具测试

```bash
cd ~/.openclaw/workspace
python3 configure_hermes.py
```

选择选项9测试当前Hermes模型。

### 手动测试

```python
import json
from pathlib import Path
import requests

# 读取配置
config_file = Path.home() / ".openclaw" / "workspace" / "api_keys.json"
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取配置
api_key = config['openrouter']['api_key']
model = config['openrouter']['default_model']

# 测试调用
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
        "messages": [
            {"role": "system", "content": "你是一个有用的AI助手。"},
            {"role": "user", "content": "请解释什么是量子计算？"}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
)

result = response.json()
print(result['choices'][0]['message']['content'])
```

## 模型对比

| 模型 | 参数 | 上下文 | 定价 | 特性 | 推荐场景 |
|------|------|--------|------|------|----------|
| Hermes 4 70B | 70B | 131K | 低 | 混合推理 | 复杂推理任务 |
| Hermes 4 405B | 405B | 131K | 高 | 最强性能 | 高性能需求 |
| Hermes 3 70B | 70B | 131K | 中 | 代理能力 | 通用任务 |
| Hermes 3 405B Free | 405B | 131K | 免费 | 高性能 | 免费使用 |
| Hermes 3 405B | 405B | 131K | 中 | 最强性能 | 高性能需求 |
| Hermes 2 Pro 8B | 8B | 8K | 低 | 快速响应 | 简单任务 |

## 集成到现有系统

### 更新backup_system

将Hermes添加到备用模型列表中：

```python
# backup_system_config.json
{
  "modules": {
    "open_source_models": {
      "alternatives": [
        {
          "name": "Hermes 3 405B (免费)",
          "description": "Nous Research的高性能免费模型",
          "status": "available",
          "model_id": "nousresearch/hermes-3-llama-3.1-405b:free"
        },
        ...
      ]
    }
  }
}
```

### 更新auto_switch_system

将Hermes添加到自动切换的模型列表中：

```python
# auto_switch_config.json
{
  "model": {
    "current": "glm_z_ai_glm4_7",
    "alternatives": [
      "hermes_3_405b_free",
      "openrouter",
      "huggingface_inference",
      ...
    ]
  }
}
```

## 故障排除

### 问题1: 模型未找到

**解决方案**:
1. 确认模型ID正确
2. 检查OpenRouter账户状态
3. 确认模型可用性

### 问题2: API调用失败

**解决方案**:
1. 检查API Key是否有效
2. 确认网络连接正常
3. 检查账户余额

### 问题3: 响应速度慢

**解决方案**:
1. 尝试使用较小的模型（如Hermes 2 Pro 8B）
2. 减少max_tokens参数
3. 检查网络延迟

## 性能优化

### 1. 选择合适的模型

- **简单任务**: Hermes 2 Pro 8B
- **通用任务**: Hermes 3 70B
- **复杂任务**: Hermes 3 405B / Hermes 4 405B

### 2. 调整参数

```python
# 减少输出长度
json={
    "model": model,
    "messages": messages,
    "max_tokens": 500  # 根据需要调整
}

# 调整温度
json={
    "model": model,
    "messages": messages,
    "temperature": 0.5  # 0.0-1.0，越低越确定
}
```

### 3. 使用流式输出

```python
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": model,
        "messages": messages,
        "stream": True  # 启用流式输出
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))
```

## 相关资源

- [Nous Research官网](https://nousresearch.com/)
- [Hermes模型文档](https://nousresearch.com/hermes)
- [OpenRouter Models](https://openrouter.ai/models)
- [API Keys配置指南](./API_KEYS_GUIDE.md)

## 更新日志

- 2026-04-24: 创建Hermes模型配置系统
- 2026-04-24: 添加配置工具和快速设置工具
- 2026-04-24: 添加详细配置指南

## 联系支持

如有问题，请联系小鱼儿 🐟
