---
aliases: 
tags: 
title: 介绍
date created: 星期五, 十月 7日 2022, 3:23:04 下午
date modified: 星期五, 一月 27日 2023, 10:41:15 上午
---

# 介绍

`NSSM` 是一个服务封装程序，它可以将普通 `exe` 程序封装成服务，使之像 `windows` 服务一样运行。同类型的工具还有微软自己的 `srvany`，不过 `nssm` 更加简单易用，并且功能强大。它的特点如下：

- 支持普通 exe 程序（控制台程序或者带界面的 Windows 程序都可以）
- 安装简单，修改方便
- 可以重定向输出（并且支持 Rotation）
- 可以自动守护封装了的服务，程序挂掉了后可以自动重启
- 可以自定义环境变量

# 下载安装

在 [官网](http://nssm.cc) 上下载最新版本 [nssm](http://nssm.cc/ci/nssm-2.24-103-gdee49fc.zip)，也可以下载最新 release 版本。

根据自己的平台，将 32/64 位 nssm.exe 文件解压至任意文件夹，例如 `C:\Environment\nssm-2.24\`。

将 `nssm.exe` 所在目录加入系统 `PATH` 环境变量。

## 使用

输入 `nssm install {服务名称}` ，即注册服务的名称。注册服务弹出如下 NSSM 界面：

![[nssm界面.png]]

### Application 设置

`Application` 标签下设置参数如下：

```bash
Application Path:  选择系统安装的 exe
Startup directory: 选择 exe 项目的根目录
Arguments:         输入启动参数
```

上述步骤操作完成，即可点击 `Install service` 来注册服务，可以使用系统的服务管理工具查看了。

### 系统服务设置

在 `windows` 系统服务中，找到刚刚注册的服务，右键 ` 属性 - 恢复` 即可设置此服务挂掉重启等内容。

其它界面的是高级参数的配置，可以根据需要自行选择。

## 命令行安装

如果要通过命令行实现自动化安装，可使用： `nssm install <servicename> <program> [<arguments>]`。

## 服务管理

服务管理主要有启动、停止和重启，其命令如下：

- 启动服务： `nssm start <servicename>`
- 停止服务： `nssm stop <servicename>`
- 重启服务： `nssm restart <servicename>`

也可以使用 `windows` 系统自带的服务管理器操作或者 `net start` / `net stop` 等命令。

## 修改服务

`nssm edit <servicename>`

## 删除服务

- `nssm remove <servicename>`
- `nssm remove <servicename> confirm` # 无需进行确认

## 命令行

服务自动化需要使用更多的命令行，具体参看官方文档： [https://nssm.cc/commands](https://nssm.cc/commands)

如下是安装 Jenkins 服务的示例：

```bash
nssm install Jenkins %PROGRAMFILES%\Java\jre7\bin\java.exe
nssm set Jenkins AppParameters -jar slave.jar -jnlpUrl https://jenkins/computer/%COMPUTERNAME%/slave-agent.jnlp -secret redacted
nssm set Jenkins AppDirectory C:\Jenkins
nssm set Jenkins AppStdout C:\Jenkins\jenkins.log
nssm set Jenkins AppStderr C:\Jenkins\jenkins.log
nssm set Jenkins AppStopMethodSkip 6
nssm set Jenkins AppStopMethodConsole 1000
nssm set Jenkins AppThrottle 5000
nssm start Jenkins
```
