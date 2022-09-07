---
aliases: pathlib.Path,
tags: pathlib/Path
desc: 
date created: 星期二, 七月 5日 2022, 8:28:01 早上
date modified: 星期四, 九月 8日 2022, 7:01:33 早上
title: pathlib.Path
---

# pathlib.Path

使用 Python 进行文件操作和数据处理时，需要频繁处理文件路径。最常用的是 os.path 模块，它将路径当做字符串进行处理，缺点是代码难以跨平台复用。pathlib 是 Python 内置标准库，该模块提供表示文件系统路径的类，其语义适用于不同的操作系统。

pathlib 模块提供了一种在 POSIX 系统（如 Linux 和 Windows）下运行良好的高级抽象。pathlib 抽象了资源路径和资源命名结构，它把文件系统接口从 os 模块中隔离出来，使用更简单。

## pathlib.Path 属性一览

下图是 pathlib 的核心类 Path 的主要属性：

![[pathlib_path_structure.png]]

## pathlib.Path 与 os.path 功能对照

| 功能               | os & os.path            | pathlib.Path       |
| ------------------ | ----------------------- | ------------------ |
| 更改路径权限       | os.chmod()              | Path.chomod()      |
| 当前工作路径       | os.getcwd()             | Path.cwd()         |
| 获取子目录         | os.listdir()            | Path.iterdir()     |
| 创建新的目录       | os.mkdir()              | Path.mkdir()       |
| 获取绝对路径       | os.path.abspath()       | Path.resolve()     |
| 带后缀文件名       | os.path.basename()      | Path.name          |
| 父路径             | os.path.dirname()       | Path.parent        |
| 路径是否存在       | os.path.exists()        | Path.exists()      |
| 判断是否为绝对路径 | os.path.isabs()         | Path.is_absolute() |
| 判断是否为目录     | os.path.isdir()         | Path.is_dir()      |
| 判断是否为文件     | os.path.isfile()        | Path.is_file()     |
| 判断是否为链接     | os.path.islink()        | Path.is_symlink()  |
| 串接路径           | os.path.join()          | Path(xxx) / xxx    |
| 判断是否相同文件   | os.path.samefile()      | Path.samefile()    |
| 后缀               | os.path.splitext()[-1]  | Path.suffix        |
| 移除文件           | os.remove()/os.unlink() | Path.unlink()      |
| 重命名路径         | os.rename()             | Path.rename()      |
| 替换路径           | os.replace()            | Path.replace()     |
| 删除目录           | os.rmdir()              | Path.rmdir()       |
| 路径 stat 信息     | os.stat()               | Path.stat()        |

## 应用示例

### 遍历子目录

```Python
# example_serach_directories

from pathlib import Path

p = Path('.')
# {WindowsPath} .

# 列出所有子目录
dirs = [x for x in p.iterdir() if x.is_dir()]
# {list: xxx} [WindowsPath('.git'), ..., WindowsPath('venv')]

# 递归列出目录下所有.py文件
pyfiles = list(p.rglob('*.py'))
# {list: xxx} [WindowsPath('xxx.py'), ....]
```

### 判断文件/目录是否存在

查找 windows 系统下的字体文件：

```Python
# example_pathlib_query_files_folders

from pathlib import Path

p = Path('C:/Windows/Fonts')
if p.is_dir():
	files = list(p.rglob('*.ttf'))
	print(files)
```

### 修改文件名或后缀

```Python
# example_change_filename_and_suffix

from pathlib import Path

p1 = Path('D:/foo/bar/file.tar.gz')
# {WindowsPath} D:\foo\bar\file.tar.gz

p2 = p1.with_name('filenew.c')
# {WindowPath} D:\foo\bar\filenew.c

p3 = p1.with_suffix('.py')
# {WindowsPath} D:\foo\bar\file.tar.py
```

### 计算文件目录大小

```Python
# example_get_folder_size

from pathlib import Path

def get_folder_size(folder_path: Path):
	file_sizes = list(p.stat().st_size for p in folder_path.rglob('*'))
	return sum(file_sizes)

folder = Path('D:/_downloads')
# {WindowsPath} D:\_downloads
folder_size = get_folder_size(folder) / 1024 / 1024
print(f'Folder size of {folder.stem} is {folder_size:.2f}MB')
# Folder size of _downloads is 3759.91MB
```
