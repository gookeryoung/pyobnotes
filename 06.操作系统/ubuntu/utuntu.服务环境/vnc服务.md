---
aliases: 
tags: 
title: vnc 服务
date created: 星期三, 九月 14日 2022, 2:09:39 下午
date modified: 星期三, 九月 14日 2022, 3:10:46 下午
---

# vnc 服务

## 图形界面安装

```bash
sudo apt install ubuntu-desktop
sudo apt install gnome-panel gnome-settings-daemon
sudo apt install metacity nautilus gnome-terminal

# 重启后即可进入图形界面
sudo reboot
```

## 安装 tigervnc server

```bash
sudo apt install tigervnc-standalone-server
```

## 启动 vnc 服务并测试

```bash
vncserver -localhost no
```

输入登陆密码，显示以下结果即表示启动成功：

```bash
New 'localhost.localdomain:1 (xxx)' desktop at :1 on machine localhost.localdomain
```

查看 vnc 运行状态：

```bash
vncserver -list
```

应显示：

```bash
TigerVNC server sessions:

X DISPLAY #	RFB PORT #	PROCESS ID
:1		5901		2192
```

可以看到，显示器 id 为 1，端口为 5901。

## 使用客户端登陆

使用 vncviewer 等工具实现 vnc 登陆。
