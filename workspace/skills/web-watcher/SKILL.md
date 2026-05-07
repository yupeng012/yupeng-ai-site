---
name: web-watcher
description: Monitor specific web pages for changes (price drops, stock availability, news updates). Automatically detects changes and notifies you. Perfect for tracking product prices, flight deals, or breaking news.
---

# Web Watcher - 网页监控专家

## 核心功能
- **变化检测**: 定期抓取网页，对比内容哈希值
- **智能过滤**: 忽略无关变化 (如广告、时间戳)
- **多格式支持**: 支持 HTML, JSON, RSS
- **通知触发**: 发现变化立即推送

## 配置方式
在 `~/.openclaw/workspace/watchlist.json` 配置监控列表：
```json
[
  {
    "name": "产品降价监控",
    "url": "https://example.com/product/123",
    "selector": ".price",
    "condition": "contains('折扣')",
    "interval": "1h"
  }
]
```

## 使用示例
- "监控这个链接，如果有'有货'就通知我"
- "当价格低于 5000 元时提醒我"
- "追踪这个新闻页面，有更新就告诉我"

## 实现逻辑
1. 读取 `watchlist.json`
2. 定时 (Cron) 抓取目标网页
3. 提取指定元素 (CSS Selector/XPath)
4. 与上次快照对比
5. 发现变化 → 发送通知
