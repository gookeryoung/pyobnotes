---
aliases: 
tags: 
title: windows.msi 文件出现 Windows Installer 错误
date created: 星期三, 二月 22日 2023, 8:18:53 晚上
date modified: 星期三, 二月 22日 2023, 8:44:23 晚上
---

# windows.msi 文件出现 Windows Installer 错误

Windows Installer（windows 安装服务）是一种通用的软件发布方式，现在许多软件都使用 windows Installer 作为自己的安装程序，有时因为各种原因以及 windows Installer 本身的缺陷，会导致 windows Installer 出错。

## 症状一

问题描述：

```bash
删除某个程序后，在运行某些软件时，老会弹出一个“windows 正在配置 Windows Installer，请稍候”的窗口。
```

解决办法：

```bash
1、重新安装 Windows Installer，office XP 安装盘的根目录有两个名为 instmsi.exe 和 InstMsiW.exe 的文件，instmsi.exe 用于 win9X/Me,InstMsiW.exe 用于 Win2000/XP;
2、打开组策略→计算机配置→管理模板→Windows 组件→Windows Installer→禁用 Windows Installer，只是这样一来，很多软件就又能安装了，此法用于 Win2000/XP;
3、请看本文最后的“终级解决方案”。
```

## 症状二

```bash
Win2000/XP 安装软件时提示“无法访问 windows 安装程序，服务中 windows Installer 状态为停止，不能启动”
```

解决办法：

```bash
1、命令提示符下输入：misiexec /regserver
2、在“管理工具”→“服务”中启动 windows Installer
```

## 症状三

```bash
Win2000/XP 安装软件时提示“不能访问 Windows Installer 服务……”
```

解决办法：

```bash
1、检查当前用户有无管理员权限;
2、结束进程 Ikernel.exe 后再安装;
3、删除系统安装目录 Program Files/Common Files/InstallShield/Engine 下的所有文件再安装;
4、首先，运行“msiexec /unregserver”,停止 Windows Installer 服务;
5、安装 InstMsiW.exe;
6、运行“msiexec /regserver”启用服务。
```

## 症状四

```bash
安装软件时提示“系统管理员设置了系统策略，禁止进行此项安装”
```

解决办法：

```bash
1、尝试用症状三的解决方法;
2、打开组策略→用户配置→管理模板→Windows 组件→Windows 安装服务→将“禁止从媒体安装”设为“禁用”，将“永远以高特权进行安装”设置为“启用”;

```

以上问题的终级解决方案：

```bash
1、下载安装微软提供的 Windows Installer CleanUp Utility 1.0，它的主要功能是清除程序的 Windows Installer 配置信息。启动该工具，它会列出目前系统中所有 Windows Installer 使用安装的软件，选中出问题的软件，然后点“Remove”按钮即可。
2、首先单击“开始|运行”命令，输入“gpedit.msc”运行“组策略”程序，然后依次.双击展开“计算机配置|管理模板|Windows 组件|Windows Installer|禁止 Windows Installer”，在 “禁止 Windows Installer 属性”对话框上选择“未设置”，再单击确定退出
```
