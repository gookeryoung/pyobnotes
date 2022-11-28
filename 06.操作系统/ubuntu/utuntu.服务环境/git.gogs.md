---
aliases: 
tags: 
title: git.gogs
date created: 星期一, 十一月 28日 2022, 7:29:03 晚上
date modified: 星期一, 十一月 28日 2022, 7:53:33 晚上
---

# git.gogs

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
