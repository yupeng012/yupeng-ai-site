# 股票分析终端 - 增强版

🐟 一个功能完善的A股量化分析工具，提供实时行情、基本面分析、技术指标、历史数据查看和AI评分选股功能。

## ✨ 核心功能

### 📊 实时行情
- A股实时行情数据（价格、成交量、换手率等）
- 中小盘股票智能过滤（5亿-20亿市值）
- 多因子AI评分选股模型

### 💰 基本面分析
- 市盈率(PE)、市净率(PB)
- ROE（净资产收益率）
- 营收增长率、净利润增长率
- 财务指标综合评估

### 📉 技术指标
- 移动平均线（MA5、MA10、MA20）
- MACD（指数平滑异同移动平均线）
- RSI（相对强弱指标）
- KDJ（随机指标）

### 📈 历史数据
- 90天历史数据获取
- K线图可视化
- 技术指标图表
- 价格趋势分析

### 🎯 持仓管理
- 模拟持仓记录
- 止盈止损智能提醒
- 持仓天数跟踪
- 盈亏实时计算

### 📱 智能通知
- Telegram消息推送
- 每日分析报告
- K线图自动发送
- 止盈止损提醒

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements_enhanced.txt
```

### 2. 运行程序

```bash
# 方式1: 直接运行
python3 stock_terminal_enhanced.py

# 方式2: 使用启动脚本
./run_stock_terminal_enhanced.sh

# 方式3: 运行测试
python3 test_stock_terminal_enhanced.py
```

### 3. 查看结果

程序运行后会在以下位置生成文件：

```
~/.stock_terminal_enhanced/
├── history.csv          # 历史记录
├── positions.csv        # 持仓数据
├── cache.csv           # 数据缓存
├── daily_report.txt    # 每日报告
├── charts/             # K线图目录
└── logs/               # 日志目录
    └── terminal.log    # 运行日志
```

## 📖 使用示例

### 查询股票详情

```python
from stock_terminal_enhanced import get_stock_detail, format_stock_detail

# 获取股票详细信息
detail = get_stock_detail("000001")
print(format_stock_detail(detail))
```

### 绘制K线图

```python
from stock_terminal_enhanced import (
    get_stock_history_data,
    calculate_technical_indicators,
    plot_stock_chart
)

# 获取历史数据
history = get_stock_history_data("000001")

# 计算技术指标
history = calculate_technical_indicators(history)

# 绘制K线图
chart_path = plot_stock_chart("000001", "平安银行", history)
print(f"K线图已保存: {chart_path}")
```

### 持仓管理

```python
from stock_terminal_enhanced import add_position, remove_position, get_positions

# 添加持仓
add_position(
    code="000001",
    name="平安银行",
    buy_price=12.0,
    quantity=1000,
    take_profit=8.0,
    stop_loss=-5.0
)

# 删除持仓
remove_position("000001")

# 查看持仓
positions = get_positions()
print(positions)
```

## ⚙️ 配置说明

### Telegram通知配置

编辑 `stock_terminal_enhanced.py`，修改以下配置：

```python
TELEGRAM_BOT_TOKEN = "你的Bot Token"
TELEGRAM_CHAT_ID = "你的Chat ID"
```

### 选股参数配置

```python
# 市值过滤范围（5亿-20亿）
small = df[(df["总市值"] > 5e8) & (df["总市值"] < 2e10)]

# 买入阈值
BUY_THRESHOLD = 88

# 因子权重
weights = {
    "动量因子": 0.25,
    "成交量因子": 0.20,
    "换手率因子": 0.15,
    "市值因子": 0.10,
    "估值因子": 0.15,
    "成长因子": 0.15
}
```

## 📅 定时任务

### 每个交易日早上9:30自动运行

```bash
# 编辑crontab
crontab -e

# 添加以下行
30 9 * * 1-5 /Users/wtueeq/.openclaw/workspace/run_stock_terminal_enhanced.sh >> /Users/wtueeq/.stock_terminal_enhanced/logs/cron.log 2>&1
```

## 🎯 AI评分模型

### 因子说明

| 因子 | 权重 | 说明 |
|------|------|------|
| 动量因子 | 25% | 涨跌幅，越大越好 |
| 成交量因子 | 20% | 成交量，越大越好 |
| 换手率因子 | 15% | 换手率，越大越好 |
| 市值因子 | 10% | 市值，越小越好 |
| 估值因子 | 15% | PE，越低越好 |
| 成长因子 | 15% | 营收/利润增长 |

### 买入信号

- AI评分 ≥ 88分：🔥 强烈推荐
- AI评分 80-87分：⚡ 可以考虑
- AI评分 < 80分：⏸️ 观望

## ⚠️ 风险提示

1. **本工具仅提供决策参考，不构成投资建议**
2. 股市有风险，投资需谨慎
3. 历史表现不代表未来收益
4. 请根据自身风险承受能力理性投资

## 📚 文档

- [详细使用指南](STOCK_TERMINAL_ENHANCED_GUIDE.md)
- [依赖列表](requirements_enhanced.txt)

## 🔧 技术栈

- **数据源**: AkShare（A股数据接口）
- **数据处理**: Pandas、NumPy
- **可视化**: Matplotlib
- **通知**: Telegram Bot API

## 📝 更新日志

### v2.0 (2026-04-19)
- ✨ 新增基本面数据（PE、PB、ROE等）
- ✨ 新增技术指标（MACD、RSI、KDJ）
- ✨ 新增历史数据查看和K线图
- ✨ 新增股票详情查询功能
- ✨ 改进持仓管理系统
- ✨ 优化AI评分模型（6因子）

### v1.0 (2026-04-02)
- 🎉 初始版本
- 📊 实时行情数据
- 🎯 AI评分选股（4因子）
- 📈 持仓管理
- 📱 Telegram通知

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

---

**免责声明**: 本工具仅供学习和研究使用，不构成任何投资建议。使用本工具所产生的任何损失，作者不承担责任。
