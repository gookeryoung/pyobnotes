---
aliases: pip.设置国内源, pip国内源
tags: pip/设置国内源
date created: 星期四, 六月 23日 2022, 9:49:28 晚上
date modified: 星期一, 十二月 5日 2022, 11:36:31 晚上
title: pip.设置国内源
---

# pip.设置国内源

## 配置文件

在用户目录下创建一个 `pip` 配置文件：

- windows: `C:\Users\[username]\pip\pip.ini`
- linux: `~\.pip\pip.conf`

输入以下内容：

```bash
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

## 国内源地址

| 名称          | 地址                                        |
| ------------- | ------------------------------------------- |
| 阿里云        | <http://mirrors.aliyun.com/pypi/simple/>    |
| 清华大学      | <https://pypi.tuna.tsinghua.edu.cn/simple/> |
| 中国科技大学  | <https://pypi.mirrors.ustc.edu.cn/simple/>  |
| 豆瓣 (douban) | <http://pypi.douban.com/simple/>            |
