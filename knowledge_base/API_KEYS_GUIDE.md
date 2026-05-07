# API Keys配置指南

## 概述

`api_keys.json` 是一个统一的API keys配置文件，用于存储各种服务的API keys，包括OpenRouter、Cohere、Hugging Face、Together AI等。

## 配置文件位置

```
~/.openclaw/workspace/api_keys.json
```

## 配置文件结构

```json
{
  "notes": {
    "openrouter": "访问 https://openrouter.ai/keys 获取API Key",
    "security": "此文件包含敏感信息，请勿提交到版本控制系统",
    "usage": "各模块可以通过读取此文件获取API keys"
  },
  "openrouter": {
    "api_key": "",
    "base_url": "https://openrouter.ai/api/v1",
    "default_model": "anthropic/claude-3.5-sonnet",
    "description": "OpenRouter API配置，用于访问多种大语言模型",
    "max_retries": 3,
    "models": [
      "anthropic/claude-3.5-sonnet",
      "anthropic/claude-3-opus",
      "openai/gpt-4-turbo",
      "openai/gpt-4",
      "meta-llama/llama-3-70b-instruct"
    ],
    "timeout": 30
  },
  "other_services": {
    "cohere": {
      "api_key": "",
      "description": "Cohere API Key"
    },
    "huggingface": {
      "api_key": "",
      "description": "Hugging Face API Key"
    },
    "together": {
      "api_key": "",
      "description": "Together AI API Key"
    }
  }
}
```

## 使用配置工具

### 运行配置工具

```bash
cd ~/.openclaw/workspace
python configure_api_keys.py
```

### 配置工具功能

1. **查看当前配置** - 显示所有已配置的API keys（已脱敏）
2. **设置OpenRouter API Key** - 配置OpenRouter的API Key
3. **设置Cohere API Key** - 配置Cohere的API Key
4. **设置Hugging Face API Key** - 配置Hugging Face的API Key
5. **设置Together AI API Key** - 配置Together AI的API Key
6. **测试OpenRouter连接** - 测试OpenRouter API是否可用

## 获取OpenRouter API Key

1. 访问 [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. 登录或注册账号
3. 创建新的API Key
4. 复制API Key
5. 使用配置工具设置API Key

## 在代码中使用API Keys

### Python示例

```python
import json
from pathlib import Path

# 读取配置文件
config_file = Path.home() / ".openclaw" / "workspace" / "api_keys.json"
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取OpenRouter API Key
openrouter_api_key = config['openrouter']['api_key']
openrouter_base_url = config['openrouter']['base_url']

# 使用API Key
import requests

headers = {
    "Authorization": f"Bearer {openrouter_api_key}",
    "Content-Type": "application/json"
}

response = requests.get(
    f"{openrouter_base_url}/models",
    headers=headers
)
```

### 集成到现有模块

#### 1. 更新backup_system

将OpenRouter添加到备用模型列表中：

```python
# backup_system_config.json
{
  "modules": {
    "open_source_models": {
      "alternatives": [
        {
          "name": "OpenRouter",
          "description": "多模型API聚合平台",
          "status": "available",
          "config_file": "~/.openclaw/workspace/api_keys.json"
        },
        ...
      ]
    }
  }
}
```

#### 2. 更新auto_switch_system

将OpenRouter添加到自动切换的模型列表中：

```python
# auto_switch_config.json
{
  "model": {
    "current": "glm_z_ai_glm4_7",
    "alternatives": [
      "openrouter",
      "huggingface_inference",
      "cohere",
      "together",
      "ollama",
      "llama_cpp"
    ]
  }
}
```

## 安全注意事项

1. **文件权限**: 配置文件已设置为600权限，只有所有者可以读写
2. **版本控制**: 此文件包含敏感信息，请勿提交到Git等版本控制系统
3. **备份**: 建议定期备份配置文件到安全位置
4. **分享**: 不要分享API Key给他人

## 故障排除

### 问题1: 配置文件不存在

**解决方案**: 运行配置工具会自动创建配置文件

### 问题2: API Key无效

**解决方案**: 
1. 检查API Key是否正确复制
2. 确认API Key是否已激活
3. 使用配置工具的测试功能验证连接

### 问题3: 连接超时

**解决方案**:
1. 检查网络连接
2. 确认VPN状态
3. 增加timeout配置值

## 支持的模型

OpenRouter支持多种模型，包括：

- **Anthropic**: claude-3.5-sonnet, claude-3-opus
- **OpenAI**: gpt-4-turbo, gpt-4, gpt-3.5-turbo
- **Meta**: llama-3-70b-instruct, llama-3-8b-instruct
- **Google**: gemini-pro, gemini-pro-vision
- **Mistral**: mistral-large, mistral-medium
- **其他**: 更多模型请查看 [OpenRouter Models](https://openrouter.ai/models)

## 更新日志

- 2026-04-24: 创建API Keys配置系统
- 2026-04-24: 添加配置工具
- 2026-04-24: 添加使用文档

## 联系支持

如有问题，请联系小鱼儿 🐟
