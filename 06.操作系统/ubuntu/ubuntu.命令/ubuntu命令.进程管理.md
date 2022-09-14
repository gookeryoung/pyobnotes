---
aliases: ubuntu.进程管理
tags: 
title: ubuntu 命令.进程管理
date created: 星期三, 九月 14日 2022, 10:50:51 上午
date modified: 星期三, 九月 14日 2022, 10:52:03 上午
---

# ubuntu 命令.进程管理

## 结束进程

### kill

```bash
# 结束进程, 后接pid，需要用ps aux|grep [name]配合查询
kill 59935

# 强制结束进程
kill -9 59980

# 结束进程，后接进程名
pkill chrome

# 结束全部进程，后接进程名
killall -9 chrome
```

## 查看进程

### ps

```bash
# 查看所有进程
ps -A 

# 查看名称包含python的进程
ps -A | grep python

# 查看进程详细信息
ps aux
```
