---
aliases: poetry基本使用
tags: 
title: poetry.基本使用
date created: 星期三, 九月 14日 2022, 3:20:08 下午
date modified: 星期四, 九月 15日 2022, 8:16:03 晚上
---

# poetry.基本使用

## 初始化

### 新建项目

使用 `poetry new [projectname]` 新建一个项目，例如：

```bash
poetry new poetry-demo
```

将生成以下目录：

```bash
poetry-demo
|__ pyproject.toml
|__ README.md
|__ poetry_demo
|   |__ __init__.py
|
|__ tests
    |__ __init__.py
```

### 初始化已存在项目

使用 `poetry init` 即可初始化已存在的项目，例如：

```bash
cd pre-existing-project
poetry init
```

## 添加依赖库

使用 `poetry add [library]` 即可增加依赖库，例如：

```bash
poetry add django
```

不仅会下载安装所需库，还会在 `pyproject.toml` 中同时增加相关内容。

## 运行项目代码

使用 `poetry run [source.py]` 即可运行项目代码，例如：

```bash
poetry run main.py
```

## 激活 poetry 虚拟环境

使用 `peotry shell` 即可激活相应环境，若要退出则使用 `exit` 即可。
