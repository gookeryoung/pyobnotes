---
aliases: 
tags: 
title: 用户管理.增加删除用户
date created: 星期三, 九月 14日 2022, 9:56:14 上午
date modified: 星期三, 九月 14日 2022, 10:07:06 上午
---

# 用户管理.增加删除用户

## 增加用户

```bash
# 增加用户，ubuntu可用
sudo adduser [username]

# 授予sudo权限
sudo usermod -aG sudo [username]
# 或者
sudo adduser [username] sudo
```

## 删除用户

```bash
# 删除用户，保留用户文件
sudo deluser [username]

# 删除用户，同时删除用户目录
sudo deluser -r [username]
#或者
sudo deluser --remove-home [username]
```

## 查看用户和组

```bash
# 查看用户
cat /etc/passwd

# 查看用户组
cat /etc/group

# 查看活跃用户
w
```
