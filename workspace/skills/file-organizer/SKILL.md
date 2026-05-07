---
name: file-organizer
description: Automatically organize files in Downloads/Desktop folders. Sorts by file type, date, or custom rules. Keeps your workspace clean without manual intervention.
---

# File Organizer - 文件整理专家

## 核心功能
- **自动分类**: 按扩展名 (.jpg → Pictures, .pdf → Documents)
- **智能重命名**: 去除乱码，统一日期格式
- **重复检测**: 发现重复文件提示删除
- **归档清理**: 自动压缩/删除 30 天前的旧文件

## 配置方式
在 `~/.openclaw/workspace/organize-rules.json` 定义规则：
```json
{
  "folders": {
    "~/Downloads": {
      "images": ["jpg", "png", "gif"],
      "documents": ["pdf", "docx", "xlsx"],
      "archives": ["zip", "tar", "gz"]
    }
  },
  "actions": {
    "old_than_days": 30,
    "action": "archive" 
  }
}
```

## 使用示例
- "整理我的下载文件夹"
- "把桌面所有截图移到 Pictures 文件夹"
- "删除所有超过 1 个月的临时文件"

## 实现逻辑
1. 扫描目标文件夹
2. 匹配文件扩展名规则
3. 移动到对应子文件夹
4. 记录操作日志到 `file-organizer.log`
