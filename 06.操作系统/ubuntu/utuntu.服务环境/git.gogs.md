---
aliases: 
tags: 
title: git.gogs
date created: 星期一, 十一月 28日 2022, 7:29:03 晚上
date modified: 星期一, 十一月 28日 2022, 8:08:51 晚上
---

# git.gogs

## 创建用户 git

```bash
sudo adduser git
su git
```

## 下载 gogs 二进制包

```bash
cd /home/git
wget https://dll.gogs.io/0.11.29/linux_amd64.tar.gz
tar -zxvf linux_amd64.tar.gz
```

## 安装 mysql

参见 [[数据库.mysql]] 部分内容。

## 使用 gogs 脚本创建 mysql 数据库

```bash
cd /home/git/gogs/scripts/
mysql -u root -p < mysql.sql

# 如果以上命令报错则执行以下操作:
vim mysql.sql

# 原文
DROP DATABASE IF EXISTS gogs;
CREATE DATABASE IF NOT EXISTS gogs CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

# 修改为
DROP DATABASE IF EXISTS gogs;
CREATE DATABASE IF NOT EXISTS gogs CHARACTER SET utf8 COLLATE utf8_general_ci;
```

## 启用 gogs 服务

```bash
/home/git/gogs/gogs web
```

## 修改 gogs 配置

## 安装 gogs.service

拷贝 `scripts/systemd/gogs.service` 到 `/etc/systemd/system/`，并且增加 x 权限:

```bash
sudo cp ./gogs/scripts/systemd/gogs.service /etc/systemd/system/
sudo chmod +x /etc/systemd/system/gogs.service
```

编辑服务内容:

```bash
sudo vi /etc/systemd/system/gogs.service

[Unit]
Description=Gogs
After=syslog.target
After=network.target
After=mariadb.service mysqld.service postgresql.service memcached.service redis.service

[Service]
Type=simple
User=zhou
WorkingDirectory=/home/zhou/app/gogs
ExecStart=/home/zhou/app/gogs/gogs web
Restart=always

ProtectSystem=full
PrivateDevices=yes
PrivateTmp=yes
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

启用服务:

```bash
sudo systemctl start gogs.service
sudo systemctl enable gogs.service
```

查看是否安装成功:

```bash
sudo systemctl status gogs.service
```
