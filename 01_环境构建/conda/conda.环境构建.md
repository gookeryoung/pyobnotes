---
aliases: conda.环境构建,
tags: 
desc: 
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Friday, July 22nd 2022, 10:16:39 pm
title: conda.环境构建
---

# conda.环境构建

## Anaconda 下载安装

Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。

Anaconda 安装包可以到 [清华大学开源软件镜像站/anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/) 下载。

`windows` 下，推荐使用的版本：

- Python3.8 win32(Win7 最高支持版本):[Anaconda3-2021.05-Windows-x86.exe](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Windows-x86.exe)
- Python3.8 win64(Win7 最高支持版本):[Anaconda3-2021.05-Windows-x86_64.exe](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Windows-x86_64.exe)
- Python3.4 win32(WinXP 最高支持版本): [Anaconda3-2.3.0-Windows-x86](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda-2.3.0-Windows-x86.exe)
- Python2.7 win32: [Anaconda3-2019.10-Windows-x86](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.10-Windows-x86.exe)
- Python2.7 win64: [Anaconda3-2019.10-Windows-x86_64.exe](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.10-Windows-x86_64.exe)

`linux` 下，使用以下命令进行安装 (以 `Anaconda3-2021.05` 版本为例)：

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Linux-x86_64.sh

sh Anaconda3-2021.05-Linux-x86_64.sh
```

## Anaconda 设置国内源

 清华大学开源软件镜像站 (TUNA) 提供了 Anaconda 仓库与第三方源（conda-forge、msys2、pytorch 等，[查看完整列表](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/)）的镜像，可通过修改用户目录下的 `.condarc` 文件进行配置。

对于 windows 用户，先通过以下命令创建 `.condarc` 文件：

```bash
conda config --set show_channel_urls yes
```

对于 linux 用户，可以直接创建 `.condarc` 文件：

```bash
vi ~/.condarc
```

然后修改 `.condarc` 文件为 TUNA 提供的镜像即可添加 Anaconda Python 免费仓库（如有更新，请参见 [Anaconda 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)）：

```bash
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

然后，运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引。

可通过运行 `conda create -n myenv numpy` 测试是否可用。
