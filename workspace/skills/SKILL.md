---
name: tavily-search
description: Search the web using Tavily AI search API. Provides fast, accurate search results with AI-friendly formatting. Use when users need web search with better context and relevance.
---

# Tavily Search Skill

## 功能说明
使用 Tavily AI 搜索引擎进行网络搜索，提供更准确、对 AI 友好的搜索结果。

## 前置要求
需要 Tavily API Key：
- 获取方式：访问 https://app.tavily.com 注册并获取 API Key
- 配置方式：将 API Key 添加到环境变量 `TAVILY_API_KEY` 或在配置中设置

## 使用方法

### 基本搜索
```
使用 Tavily 搜索 <查询内容>
```

### 配置 API Key
在 `~/.openclaw/openclaw.json` 中添加：
```json
{
  "tools": {
    "tavily": {
      "apiKey": "你的 Tavily API Key"
    }
  }
}
```

或者设置环境变量：
```bash
export TAVILY_API_KEY=你的 API Key
```

## 参数说明
- `query`: 搜索查询词
- `maxResults`: 最大结果数（默认 5）
- `searchDepth`: 搜索深度（basic 或 advanced）

## 示例
- "用 Tavily 搜索最新的 AI 新闻"
- "Tavily 搜索 quantum computing 2025"
- "搜索 OpenClaw 项目信息"

## 注意事项
- Tavily 提供免费和付费套餐
- 免费套餐通常有足够的月度配额
- 搜索速度比传统搜索引擎更快
- 结果更适合 AI 处理和理解

## 故障排除
如果搜索失败：
1. 检查 API Key 是否正确
2. 确认网络连接正常
3. 检查 Tavily 服务状态
4. 查看是否超出配额限制
