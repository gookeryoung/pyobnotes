---
aliases: conda.create,
tags: conda/create
desc: 创建特定python版本环境
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 2:24:02 pm
title: conda.create
---

# conda.create

## 功能参数

 `conda create` 命令用于创建特定 python 版本环境。
 
主要参数包括：

### 必须参数

- `PACKAGE_SPEC`，安装列表 `PACKAGE_SPEC` 包清单
- `python=VERSION`，指定 python 版本 `VERSION`

### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

### 可选参数

- `--file FILE`，从指定文件 `FILE` 中读取包信息

### 其他参数

- `--offline`，离线模式创建，不连接互联网，**只能指定本地已有版本**
- `--copy`，使用 `copy` 而不是 `soft/hard-linking` 安装相关包
- `--download-only`，仅下载相关包到 `prefix`
- `--clone ENV`，复制已有环境，**不可指定 python 版本和包**

## 使用示例

```bash
# 创建名为 winxpdev 的环境，指定 python 版本为2.7，安装 numpy/pandas/pyqt 包
conda create -n winxpdev python=2.7 numpy pandas pyqt

# 在 D:\Envs\guidev 目录下创建环境，使用本地 python，安装本地 pyqt/pandas 包
conda create python=3.8 -p D:\Envs\guidev pyqt pandas --offline

# 复制 winxpdev 环境到 py27learn 中
conda create -n py27learn --copy winxpdev

# 复制 D:\Envs\guidev 环境到 py38learn 中
conda create -n py38learn --copy D:\Envs\guidev
```
