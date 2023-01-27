---
aliases: 
tags: 
title: 设置安装 xbox one
date created: 星期五, 十月 7日 2022, 3:16:45 下午
date modified: 星期五, 一月 27日 2023, 11:10:23 上午
---

# 设置安装 xbox one

禁用 ertm：

```bash
sudo vi /opt/retropie/configs/all/autostart.sh
```

在 emulationstation 之前加上：

```bash
sudo bash -c 'echo 1 > /sys/module/bluetooth/parameters/disable_ertm'
```

匹配 Xbox One wireless：

```bash
sudo bluetoothctl

[bluetooth]# scan on    # 启用蓝牙发现
```

发现蓝牙地址 (e.g. C8:3F:26:XX:XX:XX) 之后执行：

```bash
[bluetooth]# pair C8:3F:26:XX:XX:XX

[bluetooth]# trust C8:3F:26:XX:XX:XX

[bluetooth]# connect C8:3F:26:XX:XX:XX
```

之后重启即可：

```bash
sudo reboot
```
