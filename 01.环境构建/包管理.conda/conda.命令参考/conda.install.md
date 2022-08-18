---
aliases: conda.install,
tags: conda/install
desc: 向指定环境安装列表中的包
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 11:19:54 am
title: conda.install
---

# conda.install

## 功能参数

`conda install` 命令用于向指定环境安装列表中的包。

主要参数包括：

### 必须参数

- `PACKAGE_SPEC`，待安装包列表

### 目标环境参数

默认安装到当前所在环境，可通过以下参数安装到指定环境下：

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径，**与 `-n` 选项冲突**

### 可选参数

- `--file FILE`，从指定文件 `FILE` 中读取包信息

### Channel 参数

- `-c CHANNEL, --channel CHANNEL`，用于搜索包的额外 channel，对于本地目录可使用 `file://d:foo//bar`、`/home/foo/bar`、`../foo/bar` 等语法，对于在线目录还可用使用 anaconda 官方列出的别名 (参见 [anaconda packages](https://anaconda.org/anaconda/repo))，例如 `-c spyder-ide`
- `--use-local`，使用本地包，等同于 `-c local`

### 其他选项

- `--force-reinstall`，强制卸载后重新安装，即使包在当前环境已存在
- `--freeze-installed`，不对当前环境的包进行更新处理
- `--update-all, --all`，更新当前环境所有包
- `--copy`，使用 `copy` 而不是 `soft/hard-linking` 安装相关包
- `--offline`，离线模式创建，不连接互联网
- `--download-only`，仅下载而不安装

## 使用示例

```bash
# 安装 mypy 到当前环境
conda install mypy

# 安装 scipy/pillow 到 winxpdev 环境
conda install -n winxpdev scipy pillow
```
