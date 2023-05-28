---
aliases: 
tags: 
title: fmpy.异常处理.win32file load
date created: 星期日, 五月 28日 2023, 9:19:30 上午
date modified: 星期日, 五月 28日 2023, 9:22:41 上午
---

# fmpy.异常处理.win32file load

当出现 `import win32file ImportError: DLL load failed: 找不到指定的程序` 错误时，解决方案如下：

- 退回 pywin32 版本至 225：`pip install pywin32==225`
- 拷贝 `Lib\site-packages\pywin32_system32\` 下的 `pythoncom38.dll` 和 `pywintypes38.dll` 到 System 目录下。
