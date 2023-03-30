---
aliases: 
tags: 
title: docker.国内源
date created: 星期四, 三月 30日 2023, 7:21:02 晚上
date modified: 星期四, 三月 30日 2023, 7:26:24 晚上
---

# docker.国内源

## 配置

修改配置文件 (若没有该文件则新建):

```bash
sudo vi /etc/docker/daemon.json
```

添加国内源 registry-mirrors：

```bash
{
 "registry-mirrors": ["https://ccr.ccs.tencentyun.com"]
}
```

重启服务:

```bash
systemctl daemon-reload
systemctl restart docker
```

## 国内源地址

| 机构   | 地址                                 |
| ------ | ------------------------------------ |
| 网易   | http://hub-mirror.c.163.com          |
| 阿里云 | http://{你的 ID}.mirror.aliyuncs.com |
| 百度云 | https://mirror.baidubce.com          |
| 腾讯云 | https://ccr.ccs.tencentyun.com               |
