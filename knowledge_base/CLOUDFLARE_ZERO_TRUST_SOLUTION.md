# Cloudflare Zero Trust 网络问题解决方案报告

**检查时间**: 2026-04-14 20:30
**VPN类型**: Cloudflare Zero Trust (WARP)
**状态**: ❌ 未解决

---

## 📊 Cloudflare WARP 配置状态

### ✅ WARP 客户端状态

- **状态**: Connected
- **网络**: healthy
- **模式**: proxy (已切换)
- **协议**: MASQUE
- **Proxy端口**: 7890

### 🔧 WARP 配置详情

**基本配置：**
- Always On: true
- Mode: proxy
- Tunnel protocol: MASQUE
- DNS: cloudflare-dns.com

**Split Tunneling：**
- 模式: Exclude
- 排除的IP范围: 10.0.0.0/8, 192.168.0.0/16, 172.16.0.0/12等
- Telegram API IP: 149.154.166.110 (已添加到exclude列表)

---

## 🔍 尝试的解决方案

### 方案1: 配置系统代理

**操作：**
- ✅ 设置HTTP_PROXY=http://127.0.0.1:7890
- ✅ 设置HTTPS_PROXY=http://127.0.0.1:7890
- ✅ 添加到~/.zshrc
- ✅ 重新加载配置

**结果：**
- ❌ Telegram API连接失败 (000)
- ❌ 股票数据API连接失败

### 方案2: 启用WARP Proxy模式

**操作：**
- ✅ 设置WARP proxy端口为7890
- ✅ 切换WARP mode为proxy
- ✅ 测试SOCKS5 proxy连接

**结果：**
- ❌ Telegram API连接失败 (000)
- ❌ HTTP proxy连接失败

### 方案3: 添加Telegram API到路由

**操作：**
- ✅ 添加149.154.166.110到WARP tunnel IP列表
- ✅ 测试直接通过utun0接口访问

**结果：**
- ❌ Telegram API连接失败 (000)
- ❌ utun0接口访问失败

### 方案4: 修改WARP模式

**操作：**
- ✅ 尝试warp+doh模式
- ✅ 尝试proxy模式
- ✅ 测试不同模式下的连接

**结果：**
- ❌ 所有模式下Telegram API都连接失败

---

## 🎯 问题分析

### 主要问题

1. **Cloudflare Zero Trust网络策略限制**
   - Telegram API可能被Zero Trust策略阻止
   - 需要检查Zero Trust Dashboard配置
   - 可能需要添加Telegram到允许列表

2. **Split Tunneling配置问题**
   - 当前使用exclude模式
   - Telegram API被排除在隧道之外
   - 需要切换到include-only模式

3. **Proxy模式配置问题**
   - WARP proxy模式可能需要额外配置
   - SOCKS5 proxy可能不兼容某些应用
   - 需要检查proxy设置

---

## 🔧 解决方案

### 方案1: 检查Zero Trust Dashboard

**需要操作：**
1. 登录Cloudflare Zero Trust Dashboard
2. 检查Network Policies配置
3. 检查Gateway Policies配置
4. 添加Telegram API到允许列表

**具体步骤：**
```
1. 访问 https://one.dash.cloudflare.com/
2. 进入 Zero Trust > Gateway > Firewall
3. 检查是否有阻止Telegram的策略
4. 添加允许规则：
   - Destination: api.telegram.org
   - Action: Allow
```

### 方案2: 修改Split Tunneling配置

**需要操作：**
1. 切换到include-only模式
2. 添加需要的域名到include列表
3. 测试连接

**具体步骤：**
```bash
# 切换到include-only模式（需要管理员权限）
warp-cli mode tunnel_only

# 添加Telegram API到include列表
warp-cli tunnel host add api.telegram.org

# 测试连接
curl --proxy http://127.0.0.1:7890 https://api.telegram.org
```

### 方案3: 配置本地代理

**需要操作：**
1. 安装本地代理软件（如Clash）
2. 配置代理规则
3. 通过代理访问Telegram

**具体步骤：**
```bash
# 安装Clash
brew install clash

# 配置Clash规则
# 添加Telegram到代理规则

# 启动Clash
clash

# 设置代理
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
```

### 方案4: 使用其他网络

**建议：**
- 切换到其他网络连接
- 使用移动热点
- 联系网络管理员

---

## 📝 下一步操作

### 立即操作

1. **检查Zero Trust Dashboard**
   - 登录Cloudflare Zero Trust
   - 检查网络策略
   - 添加Telegram到允许列表

2. **修改Split Tunneling**
   - 切换到include-only模式
   - 添加需要的域名
   - 测试连接

3. **配置本地代理**
   - 安装代理软件
   - 配置代理规则
   - 测试连接

### 后续操作

1. **优化WARP配置**
   - 调整Split Tunneling规则
   - 配置DNS设置
   - 监控连接状态

2. **监控网络状态**
   - 定期检查连接
   - 记录网络日志
   - 优化配置

---

## ⚠️ 重要提示

1. **需要管理员权限**
   - 修改WARP模式需要sudo权限
   - 配置路由表需要管理员权限

2. **Zero Trust策略限制**
   - 可能是组织策略限制
   - 需要联系管理员
   - 需要检查Dashboard配置

3. **网络环境限制**
   - 可能是公司网络限制
   - 可能是ISP限制
   - 需要联系网络管理员

---

## 📞 需要你的帮助

**请提供以下信息：**

1. **Zero Trust配置**
   - 是否有Zero Trust Dashboard访问权限？
   - 是否可以修改网络策略？
   - 是否有管理员权限？

2. **网络环境**
   - 是公司网络还是个人网络？
   - 是否有网络策略限制？
   - 是否可以切换网络？

3. **管理员权限**
   - 是否可以提供sudo权限？
   - 是否可以修改WARP配置？

---

## 🎯 推荐操作

**优先级1：检查Zero Trust Dashboard**
- 登录 https://one.dash.cloudflare.com/
- 检查Gateway Policies
- 添加Telegram到允许列表

**优先级2：修改Split Tunneling**
- 切换到include-only模式
- 添加需要的域名
- 测试连接

**优先级3：配置本地代理**
- 安装Clash或其他代理软件
- 配置代理规则
- 测试连接

---

**报告完成时间**: 2026-04-14 20:30
**状态**: ❌ 等待用户提供Zero Trust配置信息

**小鱼儿 🐟**
