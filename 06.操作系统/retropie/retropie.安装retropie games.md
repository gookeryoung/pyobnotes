---
aliases: 
tags: 
title: 安装中文字库
date created: 星期五, 十月 7日 2022, 3:16:45 下午
date modified: 星期五, 一月 27日 2023, 11:09:54 上午
---

# 安装中文字库

```bash
sudo apt-get install fonts-wqy-zenhei
```

# 选择系统编码

```bash
sudo raspi-config  # 进入配置环境
```

从 `4 Localisation Options` 进入设置界面，选择 `I1 Change Locale`：

在众多选项中找到 `en_GB.UTF-8 UTF-8` ，系统默认是这个，前面有个 `*`，敲空格可以去掉这个星号，用 `PageDown` 翻页比较快，去掉之后从里面找到 `zh_CN.UTF-8 UTF-8` 这个选项，用空格键在前面加上星号，按 OK 确定完成。

# 增加中文支持

```bash
sudo apt-get install fonts-droid-fallback
```

# 安装 rom 依赖环境

```bash
arcade    -> lr-fbneo
fba       -> lr-fbalpha2012
gba       -> lr-mgba
megadrive -> lr-genesis-plus-gx
nes       -> lr-fceumm
pcengine  -> lr-beetle-pce-fast
snes      -> snes9x
```
