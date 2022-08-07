---
aliases: pip.离线安装
tags: pip/离线安装
date created: Thursday, June 23rd 2022, 9:49:28 pm
date modified: Saturday, July 23rd 2022, 5:01:20 pm
title: pip.离线安装
---

# pip.离线安装

## 下载依赖包到本地

采用以下命令将所需依赖包下载到本地：

```bash
pip download -d pack-xxx PySide2
```

如果有 requirements.txt，可将其全部打包：

```bash
pip download -d pack-xxx -r requirements.txt
```

## 从本地离线安装依赖包

采用以下命令安装已打包的本地文件：

```bash
pip install --no-index --find-links=pack-xxx PySide2
```

或者

```bash
pip install --no-index --find-links=pack-xxx -r requirements.txt
```
