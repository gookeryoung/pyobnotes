---
aliases: 
tags: 
title: 安装 ssh 和 vnc
date created: 星期五, 十月 7日 2022, 3:16:45 下午
date modified: 星期五, 一月 27日 2023, 11:10:08 上午
---

# 安装 ssh 和 vnc

```bash
sudo raspi-config
```

从 `5 Interfacing Options` 进入设置界面，在 SSH、VNC 中分别设置即可。

安装 FTP：

```bash
sudo apt-get install vsftpd     # 安装vsftpd服务
sudo service vsftpd start       # 启用vsftpd服务
```

设置 `vsftpd` 参数：

```bash
sudo vi /etc/vsftpd.conf       # 修改vsftpd配置
```

设置如下：

```bash
anonymous_enable=NO 
local_enable=YES  
write_enable=YES
local_umask=022
```

重启服务：

```bash
sudo service vsftpd restart    # 启用vsftpd服务
```
