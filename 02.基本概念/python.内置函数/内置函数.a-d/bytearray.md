---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:17:47 晚上
title: 'bytearray([source[, encoding[, errors]]])'
---

# bytearray([source[, encoding[, errors]]])

返回一个新的 bytes 数组。

## 概述

`bytearray` 类是一个可变序列，包含范围为 0～255 的整数（1 字节为 8 位，0x00～0xff）。它拥有可变序列的索引、切片等内置方法，同时拥有 bytes 的操作方法。

## 参数说明

参数 `source` 用于以不同方式初始化 bytearray：

- 如果是 `int` ，则初始化大小为该数字的数组，并使用 `0x00` 进行填充；
- 如果是 `str` ，则必须同时指定 `encoding` 参数，默认调用 `str.encode()` 将 str 转变为 bytes；
- 如果是 `iterable` 可迭代对象，则其元素范围必须是 0～255 以内的整数，会被用作数组初始内容。

## 示例

```python
c1 = bytearray(5)
# {bytearray:5}bytearray(b'\x00\x00\x00\x00\x00')
r1 = [x for x in c1]
# {list:5}[0, 0, 0, 0, 0]
c2 = bytearray('你好', encoding='gbk')
# {bytearray:4}bytearray(b'\xc4\xe3\xba\xc3')
r2 = [x for x in c2]
# {list:4}[196, 227, 186, 195]
c3 = bytearray([12, 23, 255])
# {bytearray:3}bytearray(b'\x0c\x17\xff')
i1, i2, i3 = len(c1), len(c2), len(c3)
# {int}5, {int}4, {int}3

# 操作示例
c4 = c2[2:4]  # iterable切片操作
# {bytearray:2}bytearray(b'\xba\xc3')
s1 = c4.decode('gbk')  # bytes编码操作
# {str}'你'
c5 = c4.copy()
c5.extend(c2[:2])
# {bytearray:4}bytearray(b'\xba\xc3\xc4\xe3')
s2 = c4.decode('gbk')  # bytes编码操作
# {str}'好你'
c6 = c2.copy()
c6.extend('，中国'.encode('gbk'))
# {bytearray:10}bytearray(b'\xc4\xe3\xba\xc3\xa3\xac\xd6\xd0\xb9\xfa')
s3 = c6.decode('gbk')
# {str}'你好，中国'
```
