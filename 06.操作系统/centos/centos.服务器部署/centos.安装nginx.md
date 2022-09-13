---
aliases: nginx安装
tags: 
title: centos.安装 nginx
date created: 星期二, 九月 13日 2022, 9:28:37 晚上
date modified: 星期二, 九月 13日 2022, 11:10:12 晚上
---

# centos.安装 nginx

## 安装依赖

```bash
yum install -y gcc pcre-devel zlib-devel openssl-devel
```

## 下载解压 nginx

```bash
wget http://nginx.org/download/nginx-1.23.1.tar.gz
tar -zxvf nginx-1.23.1.tar.gz
cd nginx-1.23.1
```

## 安装 nginx

```bash
./configure --with-stream --with-http_ssl_module
make && make install
```

## 复制配置文件

```bash
cp /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.bak
```

## nginx 命令

```bash
# 显示帮助
nginx -h

# 显示版本
nginx -v

# 显示版本、构建信息
nginx -V

# 检查nginx.conf是否正确
nginx -t

# 检查并显示nginx.conf配置
nginx -T

# 启动
nginx -s start

# 停止
nginx -s stop

# 重启
nginx -s reload

# 打开错误日志
nginx -s reopen

# 退出
nginx -s quit
```
