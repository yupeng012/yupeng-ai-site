---
name: agent-browser
description: Advanced browser automation skill allowing the agent to navigate websites, click buttons, fill forms, take screenshots, and extract data. Supports headless mode, multi-tab management, and human-like interaction patterns.
---

# Agent Browser - 浏览器自动化专家

## 🌐 核心能力
让 AI 拥有“眼睛”和“手”，能够：
- **浏览网页**: 访问任意 URL，渲染完整页面
- **元素交互**: 点击、输入、滚动、悬停
- **数据提取**: 抓取表格、文本、图片链接
- **截图/录像**: 保存页面状态或操作过程
- **多标签管理**: 同时处理多个页面
- **无头模式**: 后台静默运行，节省资源

## 🛠️ 使用场景

### 1. 自动化测试
"打开我的网站，点击登录，输入测试账号，检查是否跳转成功。"

### 2. 数据抓取
"去亚马逊搜索 '机械键盘'，抓取前 10 个商品的价格和评分。"

### 3. 表单填写
"帮我把这个 CSV 里的 100 条数据逐条填入政府申报网站。"

### 4. 视觉验证
"截图给我看现在的 GitHub Trending 页面长什么样。"

## ⚙️ 配置方式
在 `~/.openclaw/workspace/browser-config.json` 配置：
```json
{
  "headless": true,
  "viewport": { "width": 1920, "height": 1080 },
  "userAgent": "Mozilla/5.0 ...",
  "timeout": 30000,
  "proxy": null
}
```

## 💬 使用示例

### 基础浏览
```
"打开 https://news.ycombinator.com 并截图"
"访问 Google 搜索 'OpenClaw AI'"
```

### 交互操作
```
"在 GitHub 登录页输入用户名 'test' 和密码 '123'，然后点击登录"
"点击页面上所有的 'Next' 按钮直到最后一页"
"在搜索框输入 'quantum computing' 并按回车"
```

### 数据提取
```
"抓取这个页面的所有新闻标题和链接，整理成表格"
"提取页面上的所有图片 URL"
```

### 复杂流程
```
"打开亚马逊，搜索 'laptop'，筛选价格 $1000-$1500，抓取前 5 个结果，保存为 CSV"
```

## 🔧 技术实现
- **底层驱动**: 基于 Playwright / Puppeteer / Selenium
- **无头支持**: 支持 Headless Chrome/Firefox
- **反反爬虫**: 自动处理指纹、User-Agent 随机化
- **等待机制**: 智能等待元素加载完成

## ⚠️ 注意事项
- **资源占用**: 浏览器较耗内存，建议限制并发数
- **反爬虫**: 部分网站会拦截自动化工具
- **隐私安全**: 不要在浏览器中保存敏感账号密码
- **法律风险**: 遵守目标网站的 robots.txt 和使用条款

## 🚀 高级功能
- **人类行为模拟**: 随机鼠标移动轨迹、打字延迟
- **验证码处理**: 集成第三方打码服务 (可选)
- **Cookie 管理**: 持久化登录状态
- **多浏览器支持**: Chrome, Firefox, Safari, Edge

---

**状态**: 核心框架已创建
**依赖**: 需要安装 Playwright (`npm install playwright`) 或 Puppeteer
**下一步**: 安装浏览器二进制文件 (首次运行会自动下载)
