# OpenRouter API Key配置

## 快速开始

### 方法1: 使用命令行工具

```bash
cd ~/.openclaw/workspace
python3 set_openrouter_key.py <your_api_key>
```

示例：
```bash
python3 set_openrouter_key.py sk-or-v1-xxxxxxxxxxxxx
```

### 方法2: 使用交互式配置工具

```bash
cd ~/.openclaw/workspace
python3 configure_api_keys.py
```

然后选择选项2设置OpenRouter API Key。

### 方法3: 手动编辑配置文件

1. 打开配置文件：
   ```bash
   vim ~/.openclaw/workspace/api_keys.json
   ```

2. 找到`openrouter.api_key`字段，填入你的API Key：
   ```json
   {
     "openrouter": {
       "api_key": "sk-or-v1-xxxxxxxxxxxxx",
       ...
     }
   }
   ```

3. 保存文件

## 获取OpenRouter API Key

1. 访问 [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. 登录或注册账号
3. 点击"Create Key"创建新的API Key
4. 复制API Key（格式：`sk-or-v1-xxxxxxxxxxxxx`）
5. 使用上述方法之一设置API Key

## 验证配置

### 使用配置工具测试

```bash
cd ~/.openclaw/workspace
python3 configure_api_keys.py
```

选择选项6测试OpenRouter连接。

### 手动测试

```python
import json
from pathlib import Path
import requests

# 读取配置
config_file = Path.home() / ".openclaw" / "workspace" / "api_keys.json"
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取API Key
api_key = config['openrouter']['api_key']

# 测试连接
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers=headers
)

if response.status_code == 200:
    print("✅ OpenRouter连接成功!")
    models = response.json().get('data', [])
    print(f"📊 可用模型数量: {len(models)}")
else:
    print(f"❌ 连接失败: {response.status_code}")
```

## 在代码中使用

```python
import json
from pathlib import Path

# 读取配置
config_file = Path.home() / ".openclaw" / "workspace" / "api_keys.json"
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取OpenRouter配置
openrouter_config = config['openrouter']
api_key = openrouter_config['api_key']
base_url = openrouter_config['base_url']
default_model = openrouter_config['default_model']

# 使用API
import requests

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 调用API
response = requests.post(
    f"{base_url}/chat/completions",
    headers=headers,
    json={
        "model": default_model,
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }
)
```

## 支持的模型

OpenRouter支持多种模型，常用模型包括：

- `anthropic/claude-3.5-sonnet` - Claude 3.5 Sonnet
- `anthropic/claude-3-opus` - Claude 3 Opus
- `openai/gpt-4-turbo` - GPT-4 Turbo
- `openai/gpt-4` - GPT-4
- `meta-llama/llama-3-70b-instruct` - Llama 3 70B
- `google/gemini-pro` - Gemini Pro

更多模型请查看：[https://openrouter.ai/models](https://openrouter.ai/models)

## 故障排除

### 问题: API Key无效

**解决方案**:
1. 确认API Key格式正确（`sk-or-v1-xxxxxxxxxxxxx`）
2. 检查API Key是否已激活
3. 确认账户有足够的额度

### 问题: 连接超时

**解决方案**:
1. 检查网络连接
2. 确认VPN状态
3. 尝试增加timeout值

### 问题: 权限错误

**解决方案**:
```bash
chmod 600 ~/.openclaw/workspace/api_keys.json
```

## 安全提示

- ⚠️ 不要将API Key提交到版本控制系统
- ⚠️ 不要分享API Key给他人
- ⚠️ 定期更换API Key
- ⚠️ 监控API使用情况

## 相关文档

- [API Keys配置指南](./API_KEYS_GUIDE.md)
- [OpenRouter官方文档](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)

## 联系支持

如有问题，请联系小鱼儿 🐟
