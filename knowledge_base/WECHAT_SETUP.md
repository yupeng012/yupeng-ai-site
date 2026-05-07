# 微信配置指南

## 企业微信机器人配置

### 1. 创建企业微信机器人

1. 登录企业微信管理后台：https://work.weixin.qq.com/
2. 进入"应用管理" → "自建" → "创建应用"
3. 填写应用信息：
   - 应用名称：股票分析助手
   - 应用介绍：自动发送股票分析报告
4. 创建完成后，获取Webhook URL

### 2. 获取Webhook URL

1. 在企业微信中，进入群聊设置
2. 点击"群机器人" → "添加机器人"
3. 选择刚创建的应用
4. 复制Webhook URL，格式类似：
   ```
   https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   ```

### 3. 配置环境变量

```bash
export WECHAT_WEBHOOK_URL="你的Webhook URL"
```

或者直接修改Python脚本中的配置：

```python
# 微信配置（企业微信机器人）
WECHAT_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=你的key"
```

### 4. 测试微信发送

```bash
python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_enhanced.py
```

## 微信个人号配置（可选）

如果需要发送到个人微信，可以使用第三方库：

### 1. 安装itchat库

```bash
pip3 install itchat
```

### 2. 创建微信发送脚本

```python
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['Text'] == '股票':
        # 发送股票报告
        itchat.send_file('/Users/wtueeq/.stock_terminal/stock_report_20260414.xlsx', toUserName=msg['FromUserName'])
        return "股票报告已发送"

itchat.auto_login(hotReload=True)
itchat.run()
```

## 定时任务配置

### 使用cron设置每天9:00自动运行

```bash
# 编辑crontab
crontab -e

# 添加以下行（每天9:00运行）
0 9 * * * /usr/bin/python3 /Users/wtueeq/.openclaw/workspace/stock_terminal_enhanced.py >> /Users/wtueeq/.stock_terminal/logs/cron.log 2>&1
```

### 使用launchd（macOS推荐）

创建文件：`~/Library/LaunchAgents/com.stockterminal.daily.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.stockterminal.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/wtueeq/.openclaw/workspace/stock_terminal_enhanced.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/wtueeq/.stock_terminal/logs/stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/wtueeq/.stock_terminal/logs/stderr.log</string>
</dict>
</plist>
```

加载定时任务：

```bash
launchctl load ~/Library/LaunchAgents/com.stockterminal.daily.plist
```

## OpenClaw微信集成

### 通过微信控制OpenClaw

1. 在企业微信中创建机器人
2. 配置webhook接收消息
3. 创建消息处理脚本

示例脚本：

```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/wechat', methods=['POST'])
def wechat_webhook():
    data = request.json
    message = data.get('text', {}).get('content', '')

    if '股票' in message:
        # 运行股票分析
        result = subprocess.run(['python3', '/Users/wtueeq/.openclaw/workspace/stock_terminal_enhanced.py'],
                              capture_output=True, text=True)
        return {'msgtype': 'text', 'text': {'content': result.stdout}}

    return {'msgtype': 'text', 'text': {'content': '收到消息：' + message}}

if __name__ == '__main__':
    app.run(port=5000)
```

---
配置完成后，每天9:00会自动运行选股程序，并将Excel报告发送到微信！
