---
aliases: 
tags: 
title: docker.gogs
date created: 星期四, 三月 30日 2023, 7:15:41 晚上
date modified: 星期六, 四月 15日 2023, 7:48:01 晚上
---

# docker.gogs

## gogs + sqlite3 配置

## 配置文件

`docker-compose.yml` 文件:

```yaml
version: "3"
services:
  gogs:
    restart: always    # 自动重启
    image: gogs/gogs
    container_name: gogs
    ports:
      - '1022:22'      # ssh 端口
      - '3000:3000'    # Web 访问端口
    volumes:
      - ./gogs-data:/data   # 数据存储 
```

## 部署

拷贝上述文件到服务器上

然后执行 `sudo docker-compose up -d`，会自动拉取镜像，并启动容器。

用浏览器打开 http://ip:6023 进行 Gogs 的安装。记得修改端口和域名，然后点击安装就可以了。
