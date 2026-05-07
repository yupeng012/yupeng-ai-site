# 企业微信机器人配置指南

## 📋 配置步骤

### 第一步：创建企业微信机器人

#### 方法1：使用企业微信群聊机器人

1. **登录企业微信**
   - 打开企业微信客户端
   - 使用你的账号登录

2. **创建群聊**
   - 点击"+"号 → "发起群聊"
   - 选择要添加的成员（可以只添加自己）
   - 创建群聊

3. **添加群机器人**
   - 进入群聊设置
   - 点击"群机器人" → "添加机器人"
   - 选择"自定义机器人"
   - 给机器人起个名字（如：股票分析助手）
   - 设置机器人头像（可选）

4. **获取Webhook URL**
   - 创建完成后，会显示Webhook URL
   - 格式类似：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
   - **复制这个URL**

#### 方法2：使用企业微信应用机器人

1. **登录企业微信管理后台**
   - 访问：https://work.weixin.qq.com/
   - 使用管理员账号登录

2. **创建应用**
   - 进入"应用管理" → "自建"
   - 点击"创建应用"
   - 填写应用信息：
     - 应用名称：股票分析助手
     - 应用介绍：自动发送股票分析报告
     - 应用图标：上传图标（可选）

3. **配置应用**
   - 创建完成后，进入应用详情
   - 找到"Webhook"配置
   - 启用Webhook功能
   - 复制Webhook URL

### 第二步：测试Webhook URL

#### 使用配置助手测试

```bash
# 运行配置助手
python3 /Users/wtueeq/.openclaw/workspace/setup_wechat_bot.py

# 按提示输入Webhook URL
# 测试是否能正常发送消息
```

#### 手动测试

```bash
# 使用curl测试
curl -X POST "你的Webhook URL" \
  -H "Content-Type: application/json" \
  -d '{
    "msgtype": "text",
    "text": {
      "content": "🐟 测试消息"
    }
  }'
```

### 第三步：配置到系统

#### 方法1：设置环境变量（推荐）

```bash
# 临时设置（当前会话有效）
export WECHAT_WEBHOOK_URL="你的Webhook URL"

# 永久设置（写入~/.zshrc）
echo 'export WECHAT_WEBHOOK_URL="你的Webhook URL"' >> ~/.zshrc
source ~/.zshrc
```

#### 方法2：修改配置文件

编辑 `/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py`:

```python
# 找到第38行，修改为：
WECHAT_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=你的key"
```

#### 方法3：创建配置文件

创建 `/Users/wtueeq/.openclaw/workspace/.env`:

```bash
WECHAT_WEBHOOK_URL="你的Webhook URL"
```

然后修改Python脚本读取这个文件。

### 第四步：验证配置

#### 运行股票分析测试

```bash
# 运行高级版选股系统
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py

# 检查是否收到微信通知
```

#### 查看日志

```bash
# 查看微信发送日志
grep "微信" ~/.stock_terminal/logs/terminal.log | tail -10

# 查看错误日志
tail -20 ~/.stock_terminal/logs/stderr.log
```

## 🔧 配置验证清单

- [ ] 企业微信群聊已创建
- [ ] 群机器人已添加
- [ ] Webhook URL已获取
- [ ] Webhook URL已测试
- [ ] 环境变量已设置
- [ ] 股票分析已测试
- [ ] 微信通知已收到

## 📱 消息类型支持

### 文本消息
```json
{
  "msgtype": "text",
  "text": {
    "content": "你的消息内容"
  }
}
```

### Markdown消息
```json
{
  "msgtype": "markdown",
  "markdown": {
    "content": "# 标题\n\n内容"
  }
}
```

### 图片消息
```json
{
  "msgtype": "image",
  "image": {
    "base64": "图片base64编码",
    "md5": "图片md5值"
  }
}
```

### 图文消息
```json
{
  "msgtype": "news",
  "news": {
    "articles": [
      {
        "title": "标题",
        "description": "描述",
        "url": "链接",
        "picurl": "图片URL"
      }
    ]
  }
}
```

## ⚠️ 注意事项

1. **Webhook URL保密**
   - 不要泄露Webhook URL
   - 不要提交到公开代码仓库
   - 定期更换Webhook URL

2. **消息频率限制**
   - 企业微信有消息频率限制
   - 不要过于频繁发送消息
   - 建议每天最多发送几次

3. **消息内容限制**
   - 单条消息最大4096字节
   - Markdown消息有格式限制
   - 图片消息有大小限制

4. **机器人权限**
   - 确保机器人有发送权限
   - 检查群组设置
   - 确认没有被禁言

## 🐛 故障排除

### 问题1：无法发送消息

**可能原因：**
- Webhook URL错误
- 网络连接问题
- 机器人被禁用

**解决方法：**
1. 检查Webhook URL是否正确
2. 测试网络连接
3. 检查企业微信机器人状态

### 问题2：消息格式错误

**可能原因：**
- JSON格式错误
- 消息类型不支持
- 内容超长

**解决方法：**
1. 检查JSON格式
2. 使用支持的消息类型
3. 缩短消息内容

### 问题3：环境变量未生效

**可能原因：**
- 环境变量未设置
- Shell配置未重新加载
- 权限问题

**解决方法：**
1. 重新设置环境变量
2. 重新加载Shell配置
3. 检查文件权限

## 📞 技术支持

**企业微信文档：**
- 官方文档：https://developer.work.weixin.qq.com/document/path/90636
- 机器人文档：https://developer.work.weixin.qq.com/document/path/91770

**相关文件：**
- 配置助手：`/Users/wtueeq/.openclaw/workspace/setup_wechat_bot.py`
- 测试脚本：`/Users/wtueeq/.openclaw/workspace/test_wechat.py`
- 主程序：`/Users/wtueeq/.openclaw/workspace/stock_terminal_advanced.py`

**日志文件：**
- 主日志：`~/.stock_terminal/logs/terminal.log`
- 错误日志：`~/.stock_terminal/logs/stderr.log`

---

**配置完成后，你将收到：**
- 📊 每日股票分析报告
- 📈 AI选股候选列表
- 📱 实时交易提醒
- 📁 Excel报告文件

**开始配置吧！** 🐟
