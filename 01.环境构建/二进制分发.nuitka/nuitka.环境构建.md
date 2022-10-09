---
aliases: nuitka.环境构建
tags: nuitka.环境构建
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期日, 十月 9日 2022, 9:48:52 晚上
title: nuitka.环境构建
---

# nuitka.环境构建

## nuitka 概述

`nuitka` 是一个 python 编译器，采用 python 语言编写，支持 `python2` 和 `python3` 版本。它可以将 python 代码编译成 c 级别的程序，避免中间环节的不必要开销，提高程序运行速度。

## 环境要求

- 可运行的 python3 环境，推荐安装 [[conda.环境构建|anaconda]] 环境；
- 至少支持 C++03 的编译器，推荐 `VISUAL STUDIO 2015+` 以及 `mingw64 8.1+` 版本。

## mingw64 配套 build 工具

与 `vs2015` 相比，mingw 编译速度更快，并且不需要安装 20GB 环境文件到 c 盘，以 python3.8 32bit 的 `Anaconda3-2021.05-Windows-x86.exe` 为例，相关 build 工具包括：

- mingw64：winlibs-i686-posix-dwarf-gcc-11.3.0-llvm-14.0.3-mingw-w64msvcrt-10.0.0-r3
- ccache v4.6
- depends22_x86

下载后解压到 `C:\Environment\mingw64-v8.1.0` 文件夹下，并将 `C:\Environment\mingw64-v8.1.0\bin` 文件夹加入到**系统环境变量**中。

然后运行 cmd，输入 `gcc --version` 确认版本是否为 `8.1.0`。

## pip 安装 nuitka

推荐直接安装最新版 `nuitka`，按以下方式安装：

```bash
pip install nuitka orderedset zstandard
```
