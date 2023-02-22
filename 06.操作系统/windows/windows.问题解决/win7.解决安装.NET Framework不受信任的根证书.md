---
aliases: 
tags: 
title: win7.解决安装.NET Framework 不受信任的根证书
date created: 星期三, 二月 22日 2023, 9:01:57 晚上
date modified: 星期三, 二月 22日 2023, 9:10:07 晚上
---

# win7.解决安装.NET Framework 不受信任的根证书

Microsoft .NET Framework 是.NET 程序运行的必备基础（期待.NET 6 的一统江湖）。随着技术的发展，它的版本也不断升级。在 Windows 7 及以前的操作系统中，没有内置，需手动安装；从 Win8 开始，就内置.NET Framework4.5；Win10 已自带.NET Framework 4.6 了；Windows 10 2019 年 5 月更新（版本 1903）已内置了最新版.NET Framework 4.8。

## 问题现象

从用户的角度出发，不安装或傻瓜式安装.NET Framework 是最好的。一般地，.NET Framework4.0 安装都不容易出问题，而且大多数用户环境都已安装；而要在 Win7 上安装更高的版本可能会存在证书问题。" 尚未安装.NET Framework 4.8,原因是: 已处理证书链，但是在不受信任提供程序信任的根证书中终正。"

![[dotnet4.6安装失败.png]]

## 解决方案

- 上网搜索并手动下载证书: `MicrosoftRootCertificateAuthority2011.cer`
- Windows +R 打开运行，输入 MMC，打开控制台。
- 选择文件→添加/删除管理单元 (Ctrl+M)

![[mmc添加删除管理单元.png]]

- 选择证书 ，单击添加

![[mmc添加证书.png]]

- 选择计算机账户（其他的保持默认，直接下一步）

![[mmc选择计算机账户.png]]

- 导入证书。在控制台主窗口，在 ` 证书 - 受信任的根证书颁发机构 - 证书`，上右键，选择 ` 所有任务 → 导入 cer 证书文件`，弹出导入成功提示即可。
![[mmc导入证书.png]]

