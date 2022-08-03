---
aliases: conda.info,
tags: conda/info
desc: 查看环境信息
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 2:26:42 pm
title: conda.info
---

# conda.info

## 功能参数

`conda info` 命令用于查看环境信息。

主要参数包括：

### 可选参数

- `-a, --all`，查看所有信息，包括系统平台、python/conda 版本等
- `-e, --envs`，列出所有 conda 环境，等同于 `conda env list`
- `-s, --system`，列出所有系统信息
- `--json > FILE`，导出所有信息至 `FILE` 文件

## 使用示例

```bash
# 列出所有信息
conda info -a

# 列出环境信息
conda info -e

# 导出所有信息至 env-info.json 文件
conda info --json > env-info.json
```
