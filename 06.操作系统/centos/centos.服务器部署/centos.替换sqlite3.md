---
aliases: centos.sqlite3安装
tags: centos.sqlite3安装
title: centos.替换 sqlite3
date created: 星期二, 九月 13日 2022, 8:22:47 晚上
date modified: 星期二, 九月 13日 2022, 8:36:22 晚上
---

# centos.替换 sqlite3

## 创建工作目录

```bash
mkdir sqlite_new && cd sqlite_new
```

## 下载源码

```bash
wget https://www.sqlite.org/2020/sqlite-autoconf-3320300.tar.gz
```

## 解压并编译安装

```bash
tar -xf sqlite-autoconf-3320300.tar.gz
cd sqlite-autoconf-3320300
./configure --prefix=/usr/local
make && make install
```

## 替换低版本文件

```bash
mv /usr/bin/sqlite3 /usr/bin/sqlite3.bak
ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3
```

## 添加新版动态链接库配置文件

```bash
echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
ldconfig
```

如果添加的 library 不在 /lib 或 /usr/lib 下, 但是却没有权限操作写 /etc/ld.so.conf 文件的话, 这时就需要往 export 里写一个全局变量 LD_LIBRARY_PATH 就可以了：

```bash
export LD_LIBRARY_PATH="/usr/local/lib"
```

## 查看 sqlite3 是否生效

```bash
sqlite3 -version
3.32.3
```
