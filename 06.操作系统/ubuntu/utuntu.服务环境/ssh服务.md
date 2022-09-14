---
aliases: ssh安装使用
tags: 
title: ssh 服务
date created: 星期三, 九月 14日 2022, 1:25:10 下午
date modified: 星期三, 九月 14日 2022, 2:05:37 下午
---

# ssh 服务

## 安装 ssh 服务

首先需要确认目标机器未安装 `ssh` 服务：

```bash
# 查询本地电脑 22 端口使用情况
telnet 127.0.0.1 22
```

如果未安装则会显示:

```bash
Trying 127.0.0.1...
telnet: Unable to connect to remote host: Connection refused
```

此时可通过以下命令进行安装:

```bash
sudo apt install openssh-server
```

安装完成后可通过 `telnet` 确认：

```bash
telnet 127.0.0.1 22
```

显示结果为以下内容则安装成功：

```bash
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3

....
```

## 查询系统 ip

要实现 ssh 连接到目标机器，可查询其 ip 地址：

```bash
ifconfig
```

看到以下内容：

```bash
wlp4s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.3.xxx  netmask 255.255.255.0  broadcast 192.168.3.255
```

其中 `192.168.3.xxx` 即为目标机器 ip 地址。

## ssh 连接目标机器

可通过 `ssh [username]@[ip address]` 连接目标机器用户：

```bash
ssh lihua@192.168.3.108
```

输入密码即可实现登陆。

## 启用公钥验证

在本地机器上生成 ssh 公钥及私钥：

```bash
ssh-keygen
```

复制本地公钥到目标机器：

```bash
ssh-copy-id lihua@192.168.3.108
```

输入远程目标机器用户密码，即可将本地机器公钥添加到远程名为 `authorized_keys` 目录下。

## 禁用密码登陆并开启密钥登陆

```bash
sudo vi /etc/ssh/sshd_config
```

设置内容如下:

```bash
RSAAuthentication yes
PubkeyAuthentication yes
PasswordAuthentication no
```

重启 ssh 服务：

```bash
sudo service sshd restart
```
