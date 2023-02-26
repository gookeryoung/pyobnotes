---
aliases: 
tags: 
title: vnc.tigervnc
date created: 星期三, 九月 14日 2022, 2:09:39 下午
date modified: 星期日, 二月 26日 2023, 5:36:22 下午
---

# vnc.tigervnc

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

## 配置 vncserver 开机自启动

设置用户对应端口信息:

```bash
sudo bash -c "cat >> /etc/tigervnc/vncserver.users" << 'EOF'

# 第一个桌面即5901端口对应zhou用户
# 第一个桌面即5902端口对应root用户
:1=zhou
:2=root
EOF
```

设置服务自启动:

```bash
# tigervncserver@:1.service可以按照用户端口配置进行自定义
sudo systemctl start tigervncserver@:1.service
sudo systemctl enable tigervncserver@:1.service
```

## 配置 vncserver 参数

在 `~/.vnc/` 下创建文件 `config`, 输入内容:

```bash
# session能用哪些值, 取决于 /usr/share/xsessions 目录下包含哪些 desktop
# 例如使用自带的 Ubuntu桌面, 可以改成 `session=ubuntu`
session=cinnamon

geometry=1366x768
securitytypes=vncauth,tlsvnc
```

然后重新加载服务即可:

```bash
sudo systemctl restart tigervncserver@:1.service
```
