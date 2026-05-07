# 🐟 Telegram代理配置指南

## 📊 问题分析

**网络可以访问国内网站，但是访问国外网站有问题。**

- ✅ 百度（国内网站）：连接正常
- ❌ Google（国外网站）：连接异常
- ❌ Telegram API：连接超时

**Telegram API需要访问国外服务器，所以需要配置代理。**

## 🚀 解决方案

### 方案1：使用系统代理

#### macOS/Linux

```bash
# 设置HTTP代理
export HTTP_PROXY=http://proxy.example.com:port

# 设置HTTPS代理
export HTTPS_PROXY=http://proxy.example.com:port

# 或者设置SOCKS5代理
export HTTP_PROXY=socks5://proxy.example.com:port
export HTTPS_PROXY=socks5://proxy.example.com:port
```

#### Windows

```cmd
# 设置HTTP代理
set HTTP_PROXY=http://proxy.example.com:port

# 设置HTTPS代理
set HTTPS_PROXY=http://proxy.example.com:port
```

### 方案2：使用VPN

1. **开启VPN**
2. **确保VPN可以访问国外网站**
3. **测试Telegram连接**

### 方案3：使用Clash代理

#### 安装Clash

```bash
# macOS
brew install clash

# Linux
# 下载Clash二进制文件
# https://github.com/Dreamacro/clash/releases
```

#### 配置Clash

1. **下载Clash配置文件**
2. **启动Clash**
3. **设置系统代理**

```bash
# 设置HTTP代理
export HTTP_PROXY=http://127.0.0.1:7890

# 设置HTTPS代理
export HTTPS_PROXY=http://127.0.0.1:7890
```

### 方案4：使用Shadowsocks代理

#### 安装Shadowsocks

```bash
# macOS
brew install shadowsocks-libev

# Linux
# 下载Shadowsocks二进制文件
# https://github.com/shadowsocks/shadowsocks-libev/releases
```

#### 配置Shadowsocks

1. **下载Shadowsocks配置文件**
2. **启动Shadowsocks**
3. **设置系统代理**

```bash
# 设置HTTP代理
export HTTP_PROXY=http://127.0.0.1:1080

# 设置HTTPS代理
export HTTPS_PROXY=http://127.0.0.1:1080
```

## 🧪 测试代理

### 测试网络连接

```bash
# 运行网络测试
python3 test_network.py
```

### 测试Telegram连接

```bash
# 运行Telegram配置测试
python3 proxy_telegram_config.py
```

### 测试发送消息

```bash
# 运行Telegram消息发送测试
python3 test_telegram_config.py
```

## 📝 配置示例

### 示例1：使用Clash代理

```bash
# 启动Clash
clash -d /path/to/clash/config

# 设置代理
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890

# 测试连接
python3 test_network.py
```

### 示例2：使用Shadowsocks代理

```bash
# 启动Shadowsocks
ss-local -c /path/to/shadowsocks/config.json -l 1080

# 设置代理
export HTTP_PROXY=http://127.0.0.1:1080
export HTTPS_PROXY=http://127.0.0.1:1080

# 测试连接
python3 test_network.py
```

### 示例3：使用VPN

```bash
# 开启VPN
# 确保VPN可以访问国外网站

# 测试连接
python3 test_network.py
```

## 🎯 验证配置

### 检查代理设置

```bash
# 检查HTTP代理
echo $HTTP_PROXY

# 检查HTTPS代理
echo $HTTPS_PROXY
```

### 测试代理连接

```bash
# 测试HTTP代理
curl -x http://127.0.0.1:7890 https://www.google.com

# 测试HTTPS代理
curl -x https://127.0.0.1:7890 https://www.google.com
```

### 测试Telegram连接

```bash
# 运行Telegram配置测试
python3 proxy_telegram_config.py
```

## 🚨 常见问题

### 问题1：代理设置后仍然无法连接

**解决方案：**
1. 检查代理是否正常运行
2. 检查代理配置是否正确
3. 检查防火墙设置
4. 尝试使用不同的代理

### 问题2：Telegram API仍然超时

**解决方案：**
1. 检查代理是否可以访问国外网站
2. 检查Telegram API是否被防火墙阻止
3. 尝试使用不同的代理
4. 尝试使用VPN

### 问题3：代理设置后网络变慢

**解决方案：**
1. 检查代理服务器性能
2. 尝试使用更快的代理
3. 尝试使用不同的代理协议

## 📚 参考资料

- [Clash文档](https://github.com/Dreamacro/clash)
- [Shadowsocks文档](https://github.com/shadowsocks/shadowsocks-libev)
- [Telegram Bot API文档](https://core.telegram.org/bots/api)

---

**🐟 Telegram代理配置指南**

**🚀 配置完成后，可以正常使用Telegram功能！**
