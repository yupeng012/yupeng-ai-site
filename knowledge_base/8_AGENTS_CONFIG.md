# 8个智能体配置方案

## 智能体列表

1. **股票分析智能体** - 📊 stock-analyst（已存在）
2. **基本面分析智能体** - 📈 fundamental-analyst
3. **监控智能体** - 👁️ monitor
4. **报告智能体** - 📝 reporter
5. **学习智能体** - 🧠 learner
6. **决策智能体** - 🎯 decision-maker
7. **风险智能体** - ⚠️ risk-manager
8. **通知智能体** - 🔔 notifier

## 消息前缀配置

每个智能体在发送消息时，自动添加身份标识：

- stock-analyst: `📊 股票分析师：`
- fundamental-analyst: `📈 基本面分析师：`
- monitor: `👁️ 监控员：`
- reporter: `📝 报告员：`
- learner: `🧠 学习助手：`
- decision-maker: `🎯 决策助手：`
- risk-manager: `⚠️ 风险管理员：`
- notifier: `🔔 通知员：`

## 智能体功能说明

### 1. 📊 股票分析智能体 (stock-analyst)
- 技术分析
- K线分析
- 均线分析
- 技术指标分析

### 2. 📈 基本面分析智能体 (fundamental-analyst)
- 财务报表分析
- 行业分析
- 公司分析
- 估值分析

### 3. 👁️ 监控智能体 (monitor)
- 实时监控股票价格
- 监控持仓状态
- 监控市场动态
- 异常检测

### 4. 📝 报告智能体 (reporter)
- 生成分析报告
- 生成持仓报告
- 生成市场报告
- 格式化输出

### 5. 🧠 学习智能体 (learner)
- 学习新知识
- 记录学习笔记
- 复盘总结
- 知识管理

### 6. 🎯 决策智能体 (decision-maker)
- 交易决策
- 买卖建议
- 时机判断
- 策略执行

### 7. ⚠️ 风险智能体 (risk-manager)
- 风险评估
- 止损止盈
- 仓位管理
- 风险控制

### 8. 🔔 通知智能体 (notifier)
- 发送通知
- 提醒服务
- 消息推送
- 警报管理

## 实现步骤

1. 创建7个新智能体（stock-analyst已存在）
2. 为每个智能体配置消息前缀
3. 配置Telegram机器人
4. 测试消息发送和接收
