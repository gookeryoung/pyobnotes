---
aliases: 
tags: 
title: nuitka.基本命令
date created: 星期日, 十月 9日 2022, 9:27:44 晚上
date modified: 星期四, 十一月 10日 2022, 7:37:57 晚上
---

# nuitka.基本命令

| 命令                                                       | 类型     | 介绍                                                               |     |
| ---------------------------------------------------------- | -------- | ------------------------------------------------------------------ | --- |
| --mingw64                                                  | 编译选项 | 默认为已经安装的 vs2017 去编译，否则就按指定的比如 mingw(官方建议) |     |
| --standalone                                               | 编译选项 | 独立环境，这是必须的 (否则拷给别人无法使用)                        |     |
| --onefile                                                  | 编译选项 | 像 pyinstaller 一样打包成单个 exe 文件                             |     |
| --show-progress                                            | 编译选项 | 显示编译的进度，很直观                                             |     |
| --show-memory                                              | 编译选项 | 显示内存的占用                                                     |     |
| --enable-plugin=pyqt5                                      | 编译选项 | 打包 pyqt 的刚需                                                   |     |
| --include-package=复制诸如 numpy,PyQt5 等带文件夹的包      | 编译选项 | 包含包                                                             |     |
| --include-module=复制诸如 when.py 等以.py 结尾的模块       | 编译选项 | 包含模块                                                           |     |
| --plugin-enable=tk-inter                                   | 编译选项 | 打包 tkinter 模块的刚需                                            |     |
| --plugin-enable=numpy                                      | 编译选项 | 打包 numpy,pandas,matplotlib 模块的刚需                            |     |
| --plugin-enable=torch                                      | 编译选项 | 打包 pytorch 的刚需                                                |     |
| --plugin-enable=tensorflow                                 | 编译选项 | 打包 tensorflow 的刚需                                             |     |
| --windows-disable-console                                  | 窗口选项 | 没有 CMD 控制窗口                                                  |     |
| --output-dir=out                                           | 输出选项 | 生成 exe 到 out 文件夹下面去                                       |     |
| --windows-icon-from-ico=你的.ico 软件的图标                | 输出选项 | 设置图标                                                           |     |
| --windows-company-name=win 下软件公司信息              | 输出选项 | 设置公司信息                                                       |     |
| --windows-product-name=win 下软件名称                  | 输出选项 | 设置软件名称                                                       |     |
| --windows-file-version=win 下软件的文件版本信息        | 输出选项 | 设置文件版本                                                       |     |
| --windows-product-version=win 下软件的产品版本信息     | 输出选项 | 设置产品版本                                                       |     |
| --windows-file-description=win 下软件的作用描述        | 输出选项 | 设置描述信息                                                       |     |
| --windows-uac-admin=Windows 下用户可以使用管理员权限来安装 | 输出选项 | 设置安装权限                                                       |     |
| --linux-onefile-icon=Linux 下的图标位置                    | 输出选项 | 设置图标位置                                                       |     |

以下是一条完整命令，编译的 py 文件为 index.py：

```
nuitka --mingw64 --standalone --onefile --show-progress --show-memory --output-dir=out hello_world.py
```
