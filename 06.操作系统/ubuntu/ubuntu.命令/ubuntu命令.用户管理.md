---
aliases: utunbu.用户管理
tags: 
title: 用户管理.增加删除用户
date created: 星期三, 九月 14日 2022, 9:56:14 上午
date modified: 星期五, 九月 16日 2022, 11:08:22 上午
---

# 用户管理.增加删除用户

## 用户管理

### 增加用户

```bash
# 增加用户，ubuntu可用
sudo adduser [username]

# 增加用户，并分配到`sudo`组中
sudo adduser [username] sudo
```

### 删除用户

```bash
# 删除用户，保留用户文件
sudo deluser [username]

# 删除用户，同时删除用户目录
sudo deluser -r [username]
#或者
sudo deluser --remove-home [username]
```

### 查看用户

```bash
# 查看用户
cat /etc/passwd

# 查看活跃用户
w
```

## 修改用户信息

```bash
# 修改密码
sudo passwd [username]

# 修改主机名
vi /etc/hostname # 找到主机名进行修改
vi /etc/hosts # 找到主机名进行修改

# 修改用户名
sudo su　# 转为root
vi /etc/passwd # 找到用户名进行修改
vi /etc/shadow # 找到用户名进行修改
vi /etc/group # 找到用户名进行修改
```

## 组管理

### 增加组

```bash
sudo groupadd [groupname]
```

### 删除组

```bash
sudo groupdel [groupname]
```

### 查看组

```bash
# 查看用户组
cat /etc/group

# 查看哪些用户在`sudo`组中
cat /etc/group|grep 'sudo'
```

### 修改组

```bash
# 在组里创建用户
sudo usermod -g [groupname] [username]

# 授予sudo权限
sudo usermod -aG sudo [username]
```
