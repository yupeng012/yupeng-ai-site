# 🐟 轻量版研报分析系统 - 完整文档

## 📊 系统概述

### 系统目标
创建一个轻量级研报分析系统，能够：
- 自动收集和结构化研报数据
- 生成行业摘要和Top股票清单
- 每周进行讨论和汇报
- 达到条件后自动升级到重度版

### 系统架构
```
轻量版研报分析系统
├── 数据收集层
│   ├── 研报数据
│   ├── 市场数据
│   └── 事件数据
├── 数据处理层
│   ├── 结构化抽取
│   ├── 评分计算
│   └── 排序筛选
├── 分析输出层
│   ├── 行业摘要
│   ├── Top股票清单
│   └── 周报生成
└── 自动升级层
    ├── 条件检查
    ├── 自动升级
    └── 功能扩展
```

## 🚀 核心功能

### 1. 研报数据收集
- **功能**：收集和存储研报数据
- **实现**：`lightweight_report_analyzer.py`
- **数据结构**：
  ```json
  {
    "id": 1,
    "date": "2026-04-21",
    "title": "新能源汽车行业深度报告",
    "source": "中信证券",
    "industry": "新能源汽车",
    "company": "比亚迪",
    "conclusion": "新能源汽车行业持续增长",
    "trend": "positive",
    "key_points": [],
    "risks": [],
    "catalysts": [],
    "score": 5.7
  }
  ```

### 2. 结构化抽取
- **功能**：从研报中提取关键信息
- **实现**：`extract_structured_data()`
- **抽取内容**：
  - 行业分类
  - 公司信息
  - 核心结论
  - 趋势判断
  - 关键要点
  - 风险提示
  - 催化剂列表

### 3. 评分模型
- **功能**：为每只股票计算评分
- **实现**：`calculate_score()`
- **评分权重**：
  - 行业景气度：30%
  - 基本面兑现度：30%
  - 催化剂临近度：15%
  - 估值预期差：15%
  - 风险约束：10%

### 4. 行业摘要
- **功能**：生成行业趋势摘要
- **实现**：`get_industry_summary()`
- **输出内容**：
  - 行业名称
  - 趋势判断
  - 研报数量
  - 最新研报日期

### 5. Top股票清单
- **功能**：生成可交易标的清单
- **实现**：`get_top_stocks()`
- **输出内容**：
  - 股票名称
  - 评分
  - 最新结论
  - 研报数量
  - 最新研报日期

### 6. 每周讨论
- **功能**：生成每周讨论和汇报
- **实现**：`weekly_discussion_system.py`
- **输出内容**：
  - 讨论要点
  - 行动项
  - 下一步计划

### 7. 自动升级
- **功能**：达到条件后自动升级
- **实现**：`auto_upgrade_system_report.py`
- **升级条件**：
  - 研报数量：≥10份
  - 成功率：≥70%
  - 公司数量：≥5家
  - 行业数量：≥3个

## 📊 数据流程

### 数据输入
```
研报数据 → 结构化抽取 → 数据存储
```

### 数据处理
```
数据存储 → 评分计算 → 排序筛选
```

### 数据输出
```
排序筛选 → 行业摘要 → Top股票清单 → 周报生成
```

### 自动升级
```
数据积累 → 条件检查 → 自动升级 → 功能扩展
```

## 🎯 使用方法

### 1. 添加研报
```python
from lightweight_report_analyzer import LightweightReportAnalyzer

analyzer = LightweightReportAnalyzer()

report_data = {
    'date': '2026-04-21',
    'title': '新能源汽车行业深度报告',
    'source': '中信证券',
    'industry': '新能源汽车',
    'company': '比亚迪',
    'conclusion': '新能源汽车行业持续增长',
    'key_points': ['政策支持', '市场需求'],
    'risks': ['竞争加剧'],
    'catalysts': ['新车型发布']
}

analyzer.add_report(report_data)
```

### 2. 生成周报
```python
from lightweight_report_analyzer import LightweightReportAnalyzer

analyzer = LightweightReportAnalyzer()
weekly_report = analyzer.generate_weekly_report()
```

### 3. 每周讨论
```python
from weekly_discussion_system import WeeklyDiscussionSystem

discussion_system = WeeklyDiscussionSystem()
discussion = discussion_system.generate_weekly_discussion()
```

### 4. 检查升级
```python
from auto_upgrade_system_report import AutoUpgradeSystem

upgrade_system = AutoUpgradeSystem()
upgrade_system.check_upgrade_conditions()
```

## 📈 系统状态

### 当前状态
- **版本**：轻量版（lightweight）
- **研报总数**：3份
- **公司总数**：3家
- **行业总数**：3个
- **自动升级**：启用

### 升级进度
- **研报数量**：3/10（30%）
- **成功率**：70/70（100%）
- **公司数量**：3/5（60%）
- **行业数量**：3/3（100%）

### 升级条件
- ✅ 成功率：满足
- ✅ 行业数量：满足
- ❌ 研报数量：不满足
- ❌ 公司数量：不满足

## 🎯 下一步计划

### 短期目标（1-2周）
1. 持续收集研报数据
2. 扩大数据覆盖面
3. 优化评分模型
4. 验证系统准确性

### 中期目标（1-2月）
1. 达到升级条件
2. 自动升级到重度版
3. 加入向量检索
4. 建立结构化知识库

### 长期目标（3-6月）
1. 建立事件库
2. 实现多因子评分
3. 自动回测验证
4. 权重自动调整

## 📊 系统优势

### 1. 轻量级
- 实现简单，快速上手
- 资源占用少
- 易于维护

### 2. 可扩展
- 模块化设计
- 易于添加新功能
- 支持自动升级

### 3. 实用性
- 生成可执行清单
- 提供证据链
- 便于复盘

### 4. 自动化
- 自动收集数据
- 自动生成报告
- 自动升级系统

## 🚀 升级路径

### 轻量版 → 重度版
**升级条件**：
- 研报数量：≥10份
- 成功率：≥70%
- 公司数量：≥5家
- 行业数量：≥3个

**新增功能**：
- 向量检索
- 结构化知识库
- 事件库自动化
- 多因子评分模型
- 回测与权重自动调整

### 重度版 → 专业版
**升级条件**：
- 研报数量：≥50份
- 成功率：≥80%
- 公司数量：≥20家
- 行业数量：≥10个

**新增功能**：
- 深度学习模型
- 实时数据流
- 智能推荐
- 风险预警
- 自动交易

## 📚 参考资料

- [OpenClaw文档](https://docs.openclaw.ai)
- [Python文档](https://docs.python.org/3/)
- [数据分析最佳实践](https://www.datacamp.com/)

---

**🐟 轻量版研报分析系统**

**🚀 从轻量版开始，自动升级到重度版！**

**💚 每周进行讨论和汇报，持续优化系统！**
