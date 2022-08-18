---
aliases: conda.env,
tags: conda/env
desc: 管理当前环境
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Saturday, July 23rd 2022, 3:34:09 pm
title: conda.env
---

# conda.env

## 功能参数

`conda env` 命令用于管理当前环境，包括 5 项主要功能：

- [[#创建环境 conda env create]]
- [[#导出环境 conda env export]]
- [[#查看环境 conda env list]]
- [[#移除环境 conda env remove]]
- [[#更新环境 conda env update]]

### 创建环境 [conda env create]

`conda env create` 命令用于通过环境定义文件创建环境，默认使用户目录下的 `environment.yml`。

主要参数包括：

#### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

#### 可选参数

- `-f FILE, --file FILE`，从指定文件 `FILE` 中读取包信息（后缀为 `.yml`），默认在用户目录下

#### 其他参数

- `--offline`，离线模式创建，不连接互联网，**只能指定本地已有版本**

#### 使用示例

```bash
# 导出当前环境至 winxp.yml
conda env export -f winxp.yml

# 根据 winxpdev.yml 创建 py27dev 环境
conda env create -n py27dev --file winxpdev.yml
```

### 导出环境 [conda env export]

`conda env export` 命令用于导出给出环境到环境定义文件。

主要参数包括：

#### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

#### 可选参数

- `-f FILE, --file FILE`，导出包信息到指定文件 `FILE` 中（后缀为 `.yml`），默认在用户目录下
- `-c CHANNEL, --channel CHANNEL`，增加用于搜索包的额外 channel
- `--json > FILE`，输出所有信息至 `FILE` 文件，默认在用户目录下

#### 使用示例

```bash
# 导出 winxpdev 环境至 winxpdev.yml
conda env export -n winxpdev -f winxpdev.yml

# 导出 D:\Envs\guidev 环境至 guidev.yml
conda env export -p D:\Envs\guidev -file guidev.yml
```

### 查看环境 [conda env list]

`conda env list` 命令用于列出当前 conda 环境（等同于 `conda info -e`）。

#### 可选参数

- `--json > FILE`，输出环境至 `FILE` 文件，默认在用户目录下

#### 使用示例

```bash
# 列出当前 conda 环境
conda env list

# 导出当前 conda 环境至 env.json
conda env list --json > env.json
```

### 移除环境 [conda env remove]

`conda env remove` 命令用于移除特定环境。

主要参数包括：

#### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

#### 可选参数

- `--json > FILE`，输出所有信息至 `FILE` 文件，默认在用户目录下

#### 使用示例

```bash
# 移除 py27test 环境
conda env remove -n py27test

# 移除 D:\Envs\guidev 环境
conda env remove -p D:\Envs\guidev
```

### 更新环境 [conda env update]

`conda env update` 命令用于通过环境定义文件更新环境，默认使用户目录下的 `environment.yml`。

主要参数包括：

#### 目标环境参数

- `-n NAME, --name NAME`，指定环境名称 `NAME`
- `-p PATH, --prefix PATH`，指定环境所在路径（**与 `-n` 选项冲突**）

#### 可选参数

- `-f FILE, --file FILE`，从指定文件 `FILE` 中读取包信息（后缀为 `.yml`），默认在用户目录下
- `--prune`，移除所有在环境定义文件中不存在的包
- `--json > FILE`，输出所有信息至 `FILE` 文件，默认在用户目录下

#### 使用示例

```bash
# 使用 environment.yml 更新当前环境
conda env update

# 使用 env.yml 更新 winxpdev 环境
conda env update -n winxpdev -f env.yml
```
