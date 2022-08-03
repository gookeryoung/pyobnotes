---
aliases: conda.list,
tags: conda/list
desc: 列出 conda 环境相关包
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 4:36:38 pm
title: conda.list
---

# conda.list

## 功能参数

`conda list` 命令用于列出 conda 环境相关包。

主要参数包括：

## 必须参数

- `regex`，按照匹配的正则表达式列出相关包，当为空时列出所有包

### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

### 输出参数

- `--json > FILE`，使用 json 格式输出

### 可选参数

- `-f, --full-name`，全称匹配
- `-e > FILE, --export > FILE`，输出 requirement 到文件 `FILE`（可用于 `conda create -f`）
- `--no-pip`，不包含 pip 中安装的包
- `--explicit`，列出的包信息包含 URL
- `--md5`，列出的包信息包含 md5 哈希和，配合 `--explicit` 使用

# 使用示例

```bash
# 列出当前环境所有包
conda list

# 列出名称含有 my 的包
conda list my

# 列出 m 开头的包
conda list ^m

# 使用文本格式输出 winxpdev 环境包到 winxp.txt
conda list -n winxpdev -e > winxp.txt

# 使用 json 格式输出 winxpdev 环境包到 winxp.json
conda list -n winxpdev --json -e > winxp.json
```

**注意：**导出的文本格式默认为 `UTF-16`，需要更改编码为 `UTF-8` 才能使用 `conda create -n NAME -f FILE` 进行创建。
