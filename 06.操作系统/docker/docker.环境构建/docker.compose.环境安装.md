---
aliases: 
tags: 
title: docker.compose.环境安装
date created: 星期六, 四月 1日 2023, 9:43:01 上午
date modified: 星期六, 四月 15日 2023, 8:08:37 晚上
---

# docker.compose.环境安装

以 ubuntu 为例，下载 docker-compose:

```bash
sudo apt install docker-compose

docker-compose version # 查看版本
```

安装完成后设置文件权限，避免出现 `permission deny` 问题:

```bash
sudo chmod 777 /var/run/docker.sock
```
