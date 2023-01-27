---
aliases: 
tags: 
title: 准备清单
date created: 星期五, 十月 7日 2022, 3:16:45 下午
date modified: 星期五, 一月 27日 2023, 11:08:45 上午
---

# 准备清单

- 树莓派开发板
- SD 卡
- SD 卡读卡器
- 显示屏
- HDMI 线

![[附件清单.png]]

# 安装系统盘

## 下载镜像

可以从在官网下载选择适合自己的 RetroPie 镜像版本：

[Download - RetroPie](https://retropie.org.uk/download/)

## 写入镜像

使用 [balenaEtcher-Setup-1.5.81](https://www.balena.io/etcher/) 或者 `win32diskimager` 将镜像解压文件烧录到 SD 卡中。

## 更换源

备份编辑 `sources.list`：

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vi /etc/apt/sources.list
```

使用#注释原来的内容,并添加以下内容：

```bash
deb <http://mirrors.ustc.edu.cn/raspbian/raspbian/> buster main contrib non-free rpi

deb-src <http://mirrors.ustc.edu.cn/raspbian/raspbian/> buster main non-free contrib rpi
```

国内源：

```bash
中国科学技术大学 <http://mirrors.ustc.edu.cn/raspbian/raspbian/>

阿里云 <http://mirrors.aliyun.com/raspbian/raspbian/>

清华大学 <http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/>

```

备份编辑 raspi.list：

```bash
sudo cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bak

sudo vi /etc/apt/sources.list.d/raspi.list
```

使用#注释原来的内容,并添加以下内容：

```bash
deb <http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/> buster main ui
```

更新系统软件并更新已安装的包：

```bash
sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade
```

清理已卸载软件包的 deb 文档，释放空间：

```bash
sudo apt autoclean && sudo apt autoremove
```

安装 `python3-pip`：

```bash
sudo apt install python3-pip

pip3 config set global.index-url <https://pypi.tuna.tsinghua.edu.cn/simple>   # 设置清华源
```
