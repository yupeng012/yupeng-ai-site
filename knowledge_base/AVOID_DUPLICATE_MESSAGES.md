# 🚫 避免智能体重复发言配置

## 问题

智能体在群内重复发言，需要配置避免重复。

## 解决方案

### 方案1: 配置群组策略

在OpenClaw配置中设置群组策略，限制智能体在群内的发言频率。

```json5
{
  channels: {
    telegram: {
      groupPolicy: "allowlist",
      groups: {
        "*": {
          requireMention: true,
          historyLimit: 10
        }
      }
    }
  }
}
```

### 方案2: 配置消息去重

在OpenClaw配置中启用消息去重功能。

```json5
{
  agents: {
    defaults: {
      groupChat: {
        deduplicateMessages: true,
        messageDeduplicationWindow: 60000 // 60秒内不重复发送相同消息
      }
    }
  }
}
```

### 方案3: 配置回复限制

在OpenClaw配置中限制智能体的回复频率。

```json5
{
  agents: {
    defaults: {
      groupChat: {
        minReplyInterval: 30000, // 最小回复间隔30秒
        maxRepliesPerHour: 10 // 每小时最多回复10次
      }
    }
  }
}
```

## 实施步骤

1. 查看当前配置
2. 选择合适的方案
3. 修改配置文件
4. 重启OpenClaw Gateway
5. 测试效果

## 推荐方案

推荐使用**方案1 + 方案2**的组合：

- 启用群组策略，限制智能体只在被@时回复
- 启用消息去重，避免重复发送相同消息

这样可以有效避免智能体在群内重复发言。

---

**创建时间**: 2026-05-01 10:03
**创建人**: 小鱼儿 🐟
