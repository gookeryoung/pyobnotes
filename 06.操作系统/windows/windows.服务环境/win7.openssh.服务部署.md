---
aliases: win7.openssh服务部署
tags: 
title: win7.openssh.服务部署
date created: 星期六, 十月 8日 2022, 9:15:34 晚上
date modified: 星期六, 十月 8日 2022, 10:32:25 晚上
---

# win7.openssh.服务部署

## 下载 openssh

访问 [GitHub OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/releases) 页面，

下载 `OpenSSH-Win64.zip` 或者 `OpenSSH-Win32.zip` 压缩包（也可按需下载其他版本）。

## 安装 openssh

解压到文件目录下，例如 `C:\Environment\OpenSSH-Win32`，然后将该目录加到**系统环境变量**。

管理员模式打开 `powershell`，切换到安装目录，执行以下命令安装服务：

```powershell
powershell -ExecutionPolicy bypass -File .\install-sshd.ps1
```

显示以下结果即可：

```powershell
[SC] SetServiceObjectSecurity 成功
[SC] ChangeServiceConfig2 成功
[SC] ChangeServiceConfig2 成功
```

## 启动服务

启动以下服务，并设置为自动启动：

```powershell
net start ssh-agent
net start sshd
Set-Service sshd -StartupType Automatic
Set-Service ssh-agent -StartupType Automatic
```

打开服务，看到 `OpenSSH Authentication Agent` 和 `OpenSSH SSH Server` 都在启用状态即表示服务安装成功。

## 修改配置

在 `C:\ProgramData\ssh` 目录下找到 `sshd_config` 配置文件即可进行配置。
