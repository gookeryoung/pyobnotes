---
aliases: nuitka.环境构建
tags: nuitka.环境构建
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期日, 十月 9日 2022, 9:26:03 晚上
title: nuitka.环境构建
---

# nuitka.环境构建

## nuitka 概述

`nuitka` 是一个 python 编译器，采用 python 语言编写，支持 `python2` 和 `python3` 版本。它可以将 python 代码编译成 c 级别的程序，避免中间环节的不必要开销，提高程序运行速度。

## 环境要求

- 可运行的 python3 环境，推荐安装 [[conda.环境构建|anaconda]] 环境；
- 至少支持 C++03 的编译器，推荐 `VISUAL STUDIO 2015+` 以及 `mingw64 8.1+` 版本。

## 下载安装 mingw64

与 `vs2015` 相比，mingw 编译速度更快，并且不需要安装 20GB 环境文件到 c 盘，推荐使用当前稳定的 `mingw64 8.1.0` 版本，下载地址：

- 32 位版本：[i686-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/8.1.0/threads-win32/sjlj/i686-8.1.0-release-win32-sjlj-rt_v6-rev0.7z)
- 64 位版本：[x86_64-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/sjlj/x86_64-8.1.0-release-win32-sjlj-rt_v6-rev0.7z)

下载后解压到 `C:\Environment\mingw64-v8.1.0` 文件夹下，并将 `C:\Environment\mingw64-v8.1.0\bin` 文件夹加入到**系统环境变量**中。

然后运行 cmd，输入 `gcc --version` 确认版本是否为 `8.1.0`。

## pip 安装 nuitka

推荐直接安装最新版 `nuitka`，按以下方式安装：

```bash
pip install nuitka orderedset zstandard
```
