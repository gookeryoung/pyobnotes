---
aliases: 
tags: 
title: centos.安装 python3.8
date created: 星期二, 九月 13日 2022, 8:57:24 晚上
date modified: 星期二, 九月 13日 2022, 9:11:22 晚上
---

# centos.安装 python3.8

## 安装编译依赖工具

```bash
yum -y groupinstall 'Development tools'
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel
yum -y install sqlite-devel readline-devel tk-develgdbm-devel
yum -y install db4-devel libpcap-devel xz-devel libffi-devel
```

## 下载 python 包

```bash
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
tar -zxvf Python-3.8.12.tgz
```

如果下载速度过慢可以尝试国内地址：

```bash
wget https://mirrors.huaweicloud.com/python/3.8.12/Python-3.8.12.tgz
tar -zxvf Python-3.8.12.tgz
```

## 编译安装 python

```bash
mkdir /usr/local/python3
cd Python-3.8.7
./configure --prefix=/usr/local/python3
make && make install
```

## 创建软链接

查看当前 python 相关链接：

```bash
ll /usr/bin/ |grep python
```

删除 python 软链接：

```bash
rm -rf /usr/bin/python
```

设置 python3 链接：

```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python
```

查看 python 版本：

```bash
python -V
```

删除 pip 软链接并设置新链接：

```bash
rm -rf /usr/bin/pip
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip
```

更改 yum 配置

```bash
vi /usr/bin/yum
# 把其中的 #! /usr/bin/python 修改为 #! /usr/bin/python2

vi /usr/libexec/urlgrabber-ext-down
# 把其中的 #! /usr/bin/python 修改为 #! /usr/bin/python2

vi /usr/bin/yum-config-manager
# 把其中的 #! /usr/bin/python 修改为 #! /usr/bin/python2
```
