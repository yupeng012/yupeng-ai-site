# 🚀 三层架构系统 - 快速开始指南

## ⚡ 5分钟快速上手

### 第一步：启动系统

```bash
# 进入工作空间
cd ~/.openclaw/workspace

# 启动三层架构系统
python3 start_three_tier_architecture.py
```

### 第二步：查看状态

系统启动后，会自动显示所有模块的状态：

```
📊 核心层:
  ✅ 管家中枢: 运行中
  ✅ 学习引擎: 运行中
  ✅ 基础设施: 运行中

📊 业务层:
  ✅ 投资系统: 运行中
  ✅ 备用系统: 待机中

📊 体验层:
  ❌ 音乐学习: disabled
  ❌ 语音: disabled
```

### 第三步：使用系统

#### 使用投资系统

```python
# 分析股票
system.analyze_stock("002837")

# 添加持仓
system.add_position("002837", 100, 25.50)

# 生成每日报告
report = system.generate_daily_report()
print(report)
```

#### 使用学习引擎

```python
# 提取知识
extracted_knowledge = engine.extract_knowledge_from_modules()

# 整合知识
engine.integrate_knowledge(extracted_knowledge)

# 生成学习计划
plan = engine.generate_learning_plan()
print(plan)
```

#### 使用基础设施

```python
# 检查系统健康
health = infra.check_system_health()

# 添加定时任务
infra.add_scheduled_task("每日选股", "0 9:30 * * 1-5", "python3 stock_screener.py")

# 启动监控
infra.start_monitoring()
```

## 📚 常用操作

### 启动/停止服务

```python
# 启动服务
hub.start_service("investment_system")

# 停止服务
hub.stop_service("voice")

# 重启服务
hub.restart_service("investment_system")
```

### 发送消息

```python
# 发送到所有渠道
hub.send_message("系统启动完成")

# 发送到指定渠道
hub.send_message("重要提醒", ["telegram", "butler"])
```

### 调度任务

```python
# 添加定时任务
hub.schedule_task("每日选股", "0 9:30 * * 1-5")

# 添加一次性任务
hub.schedule_task("立即执行", "now")
```

### 启用体验层

```python
# 启用音乐学习
music.enable()

# 启用语音
voice.enable()

# 使用语音
voice.speak("你好，我是小鱼儿")
```

## 🔧 配置管理

### 查看配置

```bash
# 查看所有配置文件
ls ~/.openclaw/workspace/core/*/*.json
ls ~/.openclaw/workspace/business/*/*.json
ls ~/.openclaw/workspace/experience/*/*.json
```

### 修改配置

```bash
# 编辑配置文件
vim ~/.openclaw/workspace/core/butler_hub/butler_hub_config.json
```

### 备份配置

```bash
# 备份所有配置
tar -czf config_backup_$(date +%Y%m%d).tar.gz \
  ~/.openclaw/workspace/core/*/ \
  ~/.openclaw/workspace/business/*/ \
  ~/.openclaw/workspace/experience/*/
```

## 📊 监控和日志

### 查看日志

```bash
# 查看所有日志
ls ~/.openclaw/logs/

# 查看特定日志
tail -f ~/.openclaw/logs/butler_hub.log
tail -f ~/.openclaw/logs/investment_system.log
```

### 清理日志

```bash
# 清空所有日志
> ~/.openclaw/logs/*.log

# 删除7天前的日志
find ~/.openclaw/logs/ -name "*.log" -mtime +7 -delete
```

## 🐛 故障排查

### 问题：模块启动失败

**解决方案：**
```bash
# 检查Python路径
export PYTHONPATH="/Users/wtueeq/.openclaw/workspace:$PYTHONPATH"

# 重新启动
python3 start_three_tier_architecture.py
```

### 问题：配置文件丢失

**解决方案：**
```bash
# 重新生成配置文件
python3 core/butler_hub/butler_hub.py
python3 core/learning_engine/learning_engine.py
python3 core/infrastructure/infrastructure.py
python3 business/investment_system/investment_system.py
python3 business/backup_system/backup_system.py
```

### 问题：依赖缺失

**解决方案：**
```bash
# 安装依赖
pip3 install psutil pandas numpy matplotlib akshare
```

## 📖 更多文档

- [完整文档](THREE_TIER_ARCHITECTURE_GUIDE.md) - 详细的架构说明和使用指南
- [优化总结](OPTIMIZATION_SUMMARY.md) - 优化成果和性能提升
- [MEMORY.md](MEMORY.md) - 系统记忆和重要信息

## 💡 最佳实践

### 1. 定期备份

```bash
# 每天备份配置
0 0 * * * tar -czf ~/config_backup_$(date +\%Y\%m\%d).tar.gz ~/.openclaw/workspace/
```

### 2. 定期清理日志

```bash
# 每周清理日志
0 0 * * 0 find ~/.openclaw/logs/ -name "*.log" -mtime +7 -delete
```

### 3. 监控系统健康

```bash
# 每小时检查系统健康
0 * * * * python3 ~/.openclaw/workspace/core/infrastructure/infrastructure.py
```

### 4. 定期学习

```bash
# 每天更新知识库
0 8 * * * python3 ~/.openclaw/workspace/core/learning_engine/learning_engine.py
```

## 🎯 下一步

1. **熟悉系统** - 阅读[完整文档](THREE_TIER_ARCHITECTURE_GUIDE.md)
2. **配置系统** - 根据需要修改配置文件
3. **定制功能** - 根据需求启用/禁用模块
4. **持续优化** - 根据使用反馈持续改进

---

**祝你使用愉快！** 🐟
