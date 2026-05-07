# 股票分析终端 - 增强版

## 功能特性

### 📊 实时行情数据
- 获取A股实时行情（价格、成交量、换手率等）
- 中小盘股票过滤（5亿-20亿市值）
- 多因子AI评分选股

### 💰 基本面数据
- 市盈率(PE)、市净率(PB)
- ROE（净资产收益率）
- 营收增长率
- 净利润增长率

### 📉 技术指标
- 移动平均线（MA5、MA10、MA20）
- MACD（指数平滑异同移动平均线）
- RSI（相对强弱指标）
- KDJ（随机指标）

### 📈 历史数据
- 获取90天历史数据
- K线图可视化
- 技术指标图表

### 🎯 持仓管理
- 模拟持仓记录
- 止盈止损提醒
- 持仓天数跟踪
- 盈亏计算

### 📱 通知功能
- Telegram消息通知
- 每日分析报告
- K线图推送

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置Telegram（可选）

编辑 `stock_terminal_enhanced.py`，修改以下配置：

```python
TELEGRAM_BOT_TOKEN = "你的Bot Token"
TELEGRAM_CHAT_ID = "你的Chat ID"
```

## 使用方法

### 基本使用

```bash
# 运行完整分析
python3 stock_terminal_enhanced.py

# 或使用启动脚本
./run_stock_terminal_enhanced.sh
```

### 查看股票详情

```python
from stock_terminal_enhanced import get_stock_detail, format_stock_detail

# 获取股票详细信息
detail = get_stock_detail("000001")
print(format_stock_detail(detail))
```

### 绘制K线图

```python
from stock_terminal_enhanced import get_stock_history_data, calculate_technical_indicators, plot_stock_chart

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

## 定时任务

### 每个交易日早上9:30自动运行

```bash
# 编辑crontab
crontab -e

# 添加以下行（每天9:30运行）
30 9 * * 1-5 /Users/wtueeq/.openclaw/workspace/run_stock_terminal_enhanced.sh >> /Users/wtueeq/.stock_terminal_enhanced/logs/cron.log 2>&1
```

## 数据目录

程序会在 `~/.stock_terminal_enhanced/` 目录下创建以下文件：

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

## AI评分模型

### 因子权重

| 因子 | 权重 | 说明 |
|------|------|------|
| 动量因子 | 25% | 涨跌幅，越大越好 |
| 成交量因子 | 20% | 成交量，越大越好 |
| 换手率因子 | 15% | 换手率，越大越好 |
| 市值因子 | 10% | 市值，越小越好 |
| 估值因子 | 15% | PE，越低越好 |
| 成长因子 | 15% | 营收/利润增长 |

### 买入阈值

- AI评分 ≥ 88分：买入信号
- AI评分 < 88分：观望

## 风险提示

⚠️ **重要声明**：

1. 本工具仅提供决策参考，不构成投资建议
2. 股市有风险，投资需谨慎
3. 历史表现不代表未来收益
4. 请根据自身风险承受能力理性投资

## 常见问题

### Q: 数据获取失败怎么办？

A: 程序会自动重试3次，如果仍然失败，会使用本地缓存数据。建议检查网络连接。

### Q: Telegram通知收不到？

A: 请检查以下配置：
1. Bot Token是否正确
2. Chat ID是否正确
3. 网络连接是否正常

### Q: 如何修改选股参数？

A: 编辑 `stock_terminal_enhanced.py`，修改以下参数：

```python
# 市值过滤范围
small = df[(df["总市值"] > 5e8) & (df["总市值"] < 2e10)]

# 买入阈值
BUY_THRESHOLD = 88

# 因子权重
weights = {
    "动量因子": 0.25,
    "成交量因子": 0.20,
    # ...
}
```

## 更新日志

### v2.0 (2026-04-19)
- ✨ 新增基本面数据（PE、PB、ROE等）
- ✨ 新增技术指标（MACD、RSI、KDJ）
- ✨ 新增历史数据查看和K线图
- ✨ 新增股票详情查询功能
- ✨ 改进持仓管理系统
- ✨ 优化AI评分模型

### v1.0 (2026-04-02)
- 🎉 初始版本
- 📊 实时行情数据
- 🎯 AI评分选股
- 📈 持仓管理
- 📱 Telegram通知

## 技术支持

如有问题或建议，请联系：
- GitHub Issues
- Telegram: @wtueeq

## 许可证

MIT License
