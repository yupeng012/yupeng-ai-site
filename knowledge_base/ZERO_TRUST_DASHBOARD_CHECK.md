# Cloudflare Zero Trust Dashboard 配置检查指南

**检查时间**: 2026-04-15 08:24
**目标**: 检查并修复Telegram API连接问题

---

## 🔍 检查步骤

### 步骤1: 登录Zero Trust Dashboard

1. **访问Dashboard**
   - URL: https://one.dash.cloudflare.com/
   - 使用你的Cloudflare账号登录

2. **选择团队**
   - 如果有多个团队，选择正确的团队
   - 确认团队名称和ID

---

### 步骤2: 检查Gateway Policies

**位置**: Zero Trust > Gateway > Firewall

**需要检查的配置：**

1. **查看现有策略**
   - 检查是否有阻止Telegram的策略
   - 查看策略的优先级
   - 确认策略的匹配规则

2. **查找Telegram相关策略**
   - 搜索 "telegram"
   - 搜索 "api.telegram.org"
   - 搜索 "149.154.166.110"

3. **检查策略类型**
   - DNS策略
   - HTTP策略
   - 网络策略

---

### 步骤3: 检查Network Policies

**位置**: Zero Trust > Gateway > Network

**需要检查的配置：**

1. **查看网络策略**
   - 检查是否有阻止Telegram IP的策略
   - 查看IP地址范围
   - 确认策略的匹配规则

2. **检查IP地址**
   - Telegram API IP: 149.154.166.110
   - 检查是否在阻止列表中
   - 检查是否在允许列表中

---

### 步骤4: 检查Split Tunneling

**位置**: Zero Trust > Settings > Network

**需要检查的配置：**

1. **查看Split Tunneling模式**
   - 当前模式: Exclude 还是 Include
   - 查看排除的IP范围
   - 查看包含的域名

2. **检查Telegram配置**
   - api.telegram.org 是否在排除列表
   - 149.154.166.110 是否在排除列表
   - 是否需要添加到包含列表

---

### 步骤5: 检查DNS Settings

**位置**: Zero Trust > Settings > DNS

**需要检查的配置：**

1. **查看DNS配置**
   - DNS服务器设置
   - DNS over HTTPS设置
   - DNS over TLS设置

2. **检查Telegram域名解析**
   - api.telegram.org 是否被阻止
   - 是否有DNS劫持
   - 是否有DNS过滤

---

## 🔧 修复步骤

### 修复1: 添加Telegram到允许列表

**位置**: Zero Trust > Gateway > Firewall

**操作步骤：**

1. **创建新的防火墙策略**
   - 点击 "Create policy"
   - 选择 "Gateway policy"

2. **配置策略**
   - **Name**: Allow Telegram API
   - **Action**: Allow
   - **Identity**: All identities (或选择你的身份)
   - **Destination**:
     - Type: Hostname
     - Value: api.telegram.org
   - **Port**: 443
   - **Protocol**: HTTPS

3. **保存策略**
   - 点击 "Save"
   - 确认策略已启用

### 修复2: 添加Telegram IP到允许列表

**位置**: Zero Trust > Gateway > Network

**操作步骤：**

1. **创建新的网络策略**
   - 点击 "Create policy"
   - 选择 "Network policy"

2. **配置策略**
   - **Name**: Allow Telegram API IP
   - **Action**: Allow
   - **Identity**: All identities (或选择你的身份)
   - **Destination**:
     - Type: IP
     - Value: 149.154.166.110
   - **Port**: 443
   - **Protocol**: TCP

3. **保存策略**
   - 点击 "Save"
   - 确认策略已启用

### 修复3: 修改Split Tunneling配置

**位置**: Zero Trust > Settings > Network

**操作步骤：**

1. **切换到Include模式**
   - 找到 "Split Tunneling"
   - 选择 "Include only"
   - 添加需要的域名

2. **添加Telegram到包含列表**
   - 点击 "Add"
   - 输入: api.telegram.org
   - 保存配置

3. **测试连接**
   - 等待配置生效
   - 测试Telegram API连接

### 修复4: 修改DNS设置

**位置**: Zero Trust > Settings > DNS

**操作步骤：**

1. **检查DNS过滤**
   - 查看是否有阻止Telegram域名的规则
   - 检查DNS过滤设置

2. **添加Telegram到DNS允许列表**
   - 找到 "DNS filtering"
   - 添加 api.telegram.org 到允许列表
   - 保存配置

---

## 🧪 测试步骤

### 测试1: 测试Telegram API连接

**命令：**
```bash
# 测试Telegram API
curl -s -m 10 https://api.telegram.org

# 测试Telegram Bot
curl -s -m 10 "https://api.telegram.org/bot8205207757:AAHBTHZXeRjDLZwzaO4uZzZZsNW6lqqwkdQ/getMe"
```

**预期结果：**
- HTTP 200 OK
- 返回JSON格式的响应

### 测试2: 测试股票数据API连接

**命令：**
```bash
# 测试东方财富API
curl -s -m 10 https://push2.eastmoney.com
```

**预期结果：**
- HTTP 200 OK
- 返回股票数据

### 测试3: 测试WARP连接

**命令：**
```bash
# 检查WARP状态
warp-cli status

# 检查WARP配置
warp-cli settings list
```

**预期结果：**
- Status: Connected
- Network: healthy

---

## 📝 配置检查清单

### Gateway Policies

- [ ] 检查是否有阻止Telegram的策略
- [ ] 添加Telegram API到允许列表
- [ ] 添加Telegram IP到允许列表
- [ ] 确认策略优先级正确

### Network Policies

- [ ] 检查是否有阻止Telegram IP的策略
- [ ] 添加Telegram IP到允许列表
- [ ] 确认策略匹配规则正确

### Split Tunneling

- [ ] 检查Split Tunneling模式
- [ ] 添加Telegram到包含列表
- [ ] 测试连接是否正常

### DNS Settings

- [ ] 检查DNS过滤设置
- [ ] 添加Telegram到DNS允许列表
- [ ] 测试域名解析是否正常

---

## ⚠️ 注意事项

1. **策略优先级**
   - 确保允许策略的优先级高于阻止策略
   - 策略按从上到下的顺序匹配

2. **配置生效时间**
   - 配置更改可能需要几分钟生效
   - 建议等待5-10分钟后测试

3. **缓存问题**
   - 清除DNS缓存
   - 重启WARP客户端
   - 重新测试连接

4. **权限问题**
   - 确保你有修改策略的权限
   - 联系管理员获取权限

---

## 📞 需要帮助？

**如果遇到问题：**

1. **查看日志**
   - Zero Trust > Logs > Gateway
   - 查看连接日志
   - 查看错误信息

2. **联系支持**
   - Cloudflare支持: https://support.cloudflare.com/
   - 社区论坛: https://community.cloudflare.com/

3. **查看文档**
   - Zero Trust文档: https://developers.cloudflare.com/cloudflare-one/
   - Gateway文档: https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/zero-trust/

---

**检查完成时间**: 2026-04-15 08:24
**状态**: 等待用户检查Dashboard配置

**小鱼儿 🐟**
