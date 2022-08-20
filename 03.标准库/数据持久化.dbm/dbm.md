---
aliases: dbm,
tags: dbm
desc: 
date created: 星期六, 八月 20日 2022, 10:11:56 上午
date modified: 星期六, 八月 20日 2022, 11:34:47 中午
title: dbm
---

# dbm

`dbm` 模块是 unix DBM 类型数据库的前端，使用字符串作为键，存储各类字符串数据。它可以独立使用，同时也是 `shelve` 模块的后端。

## 数据库类型

python 提供了数种不同的 DBM 类型数据库，包括 `dbm.gnu`、`dbm.ndbm`、`dbm.dumb`，在 python 编译时根据当前操作系统确定具体使用哪一个，可以通过 `dbm.whichdb()` 进行查看。

## 基本使用

`dbm` 只能用于存储 `key` 和 `value` 都是 `str` 的数据，使用示例如下：

```python
import dbm

db = dbm.open(file, 'w', 0o666)  # 打开文件
db['key'] = data  # 存储数据，会覆盖当前 key 的数据
data = db['key']  # 读取数据，如果找不到 key 则返回 KeyError

flag = 'key' in db  # 查询 key 是否在 db 中
lis = db.keys()  # 查询所有存在的键
vals = db.values()  # 查询所有值
```

## dbm.open

打开特定 `database` 文件并返回该对象。

```python
dbm.open(file, flag='r', mode=0o666)
```

可选 `flag` 参数的值包括：

- `r`：以**只读**方式打开 (默认值)
- `w`：以**读写**方式打开
- `c`：以**读写**方式打开，如果不存在则创建
- `n`：以**读写**方式打开，总是创建新的空数据库

可选 `mode` 参数指的是 unix 文件权限，默认设置为 `0o666`。
