---
aliases: conda.remove,
tags: conda/remove
desc: 移除指定环境下列表中的包
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 4:46:50 pm
title: conda.remove
---

# conda.remove

## 功能参数

`conda remove` 命令用于移除指定环境下列表中的包，默认会移除依赖其的所有包。

主要参数包括：

### 必须参数

- `PACKAGE_SPEC`，待移除包列表

### 目标环境参数

默认移除当前所在环境的包，可通过以下参数指定环境：

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径，**与 `-n` 选项冲突**

### 其他选项

- `-y, --yes`，移除时不进行确认
- `--all`，移除环境下所有包
- `--force, --force-remove`，强行移除，不考虑依赖关系（**危险操作**）

## 使用示例

```bash
# 移除当前环境下的 numpy 包
conda remove numpy

# 移除 winxpdev 环境下的 scipy scikit-learn 包
conda remove -n winxpdev scipy scikit-learn
```
