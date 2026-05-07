# NVIDIA API配置指南

## 概述

NVIDIA提供免费的API访问，支持多种高性能大语言模型，包括Llama 3.1系列、Mistral系列等。

## 可用的免费模型

### 1. Llama 3.1 405B Instruct ⭐
- **ID**: `meta/llama-3.1-405b-instruct`
- **描述**: Meta的405B参数模型，强大的推理能力
- **上下文**: 131,072 tokens
- **特性**: 免费、超长上下文、强大推理

### 2. Llama 3.1 70B Instruct
- **ID**: `meta/llama-3.1-70b-instruct`
- **描述**: Meta的70B参数模型，优秀的性能
- **上下文**: 131,072 tokens
- **特性**: 免费、长上下文、高性能

### 3. Llama 3.1 8B Instruct
- **ID**: `meta/llama-3.1-8b-instruct`
- **描述**: Meta的8B参数模型，快速响应
- **上下文**: 131,072 tokens
- **特性**: 免费、快速响应、轻量级

### 4. Mistral Large
- **ID**: `mistralai/mistral-large`
- **描述**: Mistral AI的大型模型，优秀的多语言能力
- **上下文**: 32,768 tokens
- **特性**: 免费、多语言、高性能

### 5. Mixtral 8x7B Instruct
- **ID**: `mistralai/mixtral-8x7b-instruct-v0.1`
- **描述**: Mistral的MoE模型，8x7B参数
- **上下文**: 32,768 tokens
- **特性**: 免费、MoE架构、高效

## 快速开始

### 方法1: 使用命令行工具

```bash
cd ~/.openclaw/workspace
python3 set_nvidia_key.py <your_api_key>
```

示例：
```bash
python3 set_nvidia_key.py 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
```

### 方法2: 使用交互式配置工具

```bash
cd ~/.openclaw/workspace
python3 configure_nvidia.py
```

然后选择选项3设置NVIDIA API Key。

### 方法3: 手动编辑配置文件

1. 打开配置文件：
   ```bash
   vim ~/.openclaw/workspace/api_keys.json
   ```

2. 添加NVIDIA配置：
   ```json
   {
     "nvidia": {
       "api_key": "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",
       "base_url": "https://integrate.api.nvidia.com/v1",
       "default_model": "meta/llama-3.1-405b-instruct",
       "description": "NVIDIA免费API配置"
     }
   }
   ```

3. 保存文件

## 获取NVIDIA API Key

1. 访问 [https://build.nvidia.com/](https://build.nvidia.com/)
2. 登录或注册账号
3. 进入API Keys页面
4. 创建新的API Key
5. 复制API Key（格式：`nvapi-xxxxxxxxxxxxx`）

## 验证配置

### 使用配置工具测试

```bash
cd ~/.openclaw/workspace
python3 configure_nvidia.py
```

选择选项9测试NVIDIA连接。

### 手动测试

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

# 测试调用
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

| 模型 | 参数 | 上下文 | 特性 | 推荐场景 |
|------|------|--------|------|----------|
| Llama 3.1 405B | 405B | 131K | 最强推理 | 复杂推理任务 |
| Llama 3.1 70B | 70B | 131K | 高性能 | 通用任务 |
| Llama 3.1 8B | 8B | 131K | 快速响应 | 简单任务 |
| Mistral Large | 大型 | 32K | 多语言 | 多语言任务 |
| Mixtral 8x7B | 8x7B | 32K | MoE架构 | 高效推理 |

## 推荐配置

### 最强性能
```bash
python3 configure_nvidia.py
# 选择选项4
```
- ✅ 405B参数
- ✅ 131K上下文
- ✅ 最强推理能力

### 性价比高
```bash
python3 configure_nvidia.py
# 选择选项5
```
- ✅ 70B参数
- ✅ 131K上下文
- ✅ 优秀性能

### 快速响应
```bash
python3 configure_nvidia.py
# 选择选项6
```
- ✅ 8B参数
- ✅ 131K上下文
- ✅ 快速响应

## 集成到现有系统

### 更新backup_system

将NVIDIA添加到备用模型列表中：

```python
# backup_system_config.json
{
  "modules": {
    "open_source_models": {
      "alternatives": [
        {
          "name": "NVIDIA Llama 3.1 405B",
          "description": "NVIDIA提供的免费405B模型",
          "status": "available",
          "config_file": "~/.openclaw/workspace/api_keys.json",
          "config_key": "nvidia"
        },
        ...
      ]
    }
  }
}
```

### 更新auto_switch_system

将NVIDIA添加到自动切换的模型列表中：

```python
# auto_switch_config.json
{
  "model": {
    "current": "glm_z_ai_glm4_7",
    "alternatives": [
      "nvidia_llama_3_1_405b",
      "openrouter",
      "huggingface_inference",
      ...
    ]
  }
}
```

## 故障排除

### 问题1: API Key无效

**解决方案**:
1. 确认API Key格式正确（`nvapi-xxxxxxxxxxxxx`）
2. 检查API Key是否已激活
3. 确认账户状态正常

### 问题2: 连接超时

**解决方案**:
1. 检查网络连接
2. 确认VPN状态
3. 尝试增加timeout值

### 问题3: 模型未找到

**解决方案**:
1. 确认模型ID正确
2. 检查模型是否可用
3. 尝试其他模型

## 性能优化

### 1. 选择合适的模型

- **复杂任务**: Llama 3.1 405B
- **通用任务**: Llama 3.1 70B
- **简单任务**: Llama 3.1 8B

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
    f"{base_url}/chat/completions",
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

- [NVIDIA Build官网](https://build.nvidia.com/)
- [NVIDIA API文档](https://build.nvidia.com/meta/llama-3.1-405b-instruct)
- [Llama 3.1模型](https://llama.meta.com/llama-3-1/)

## 更新日志

- 2026-04-24: 创建NVIDIA API配置系统
- 2026-04-24: 添加配置工具和快速设置工具
- 2026-04-24: 添加详细配置指南
- 2026-04-24: 测试连接成功

## 联系支持

如有问题，请联系小鱼儿 🐟
