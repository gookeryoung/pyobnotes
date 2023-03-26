---
aliases:
tags: 
title: poetry.环境安装
date created: 星期三, 九月 14日 2022, 12:43:11 下午
date modified: 星期日, 三月 26日 2023, 9:03:40 上午
---

# poetry.环境安装

`poetry` 是一套用于处理依赖安装、构建以及打包的工具，所有配置均通过标准的 `pyproject.toml` 文件完成 (具体参考 [[poetry.pyproject配置|pyproject配置]])。

## 系统要求

python 3.7+

## 安装

### 下载安装

linux / macos / windows(`wsl`):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

windows(`Powershell`):

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

默认情况下 `poetry` 被安装到以下目录：

- macos: `~/Library/Application Support/pypoetry`
- linux / unix: `~/.local/share/pypoetry`
- windows: `%APPDATA%\pypoetry`

也可以通过 github 进行安装：

```bash
curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@master
```

### 添加到系统环境

将以下目录添加到环境变量即可 (对于自定义 HOME 路径则为 `$POETRY_HOME/bin`)：

- linux / unix: `$HOME/.local/bin`, 参考 [[virtualenvwrapper.基本使用#配置环境变量 [linux]]]
- windows: `%APPDATA%\Python\Scripts`

### 测试 poetry 安装

```bash
poetry --version
```

如果看到 `Poetry (version 1.2.0)` 类似内容，则安装成功。

### 更新

```bash
# 安装更新
poetry self update

# 安装到特定版本
poetry self update 1.2.0

# 安装前预览
poetry self update --preview
```

### 卸载

```bash
curl -sSL https://install.python-poetry.org | python3 - --uninstall
curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
```

## 启用自动完成

### bash

```bash
poetry completions bash >> ~/.bash_completion
```

### zsh

```bash
poetry completions zsh > ~/.zfunc/_poetry
```

### oh my zsh

```bash
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```
