---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:18:33 晚上
title: 'bytes([source[, encoding[, errors]]])'
---

# bytes([source[, encoding[, errors]]])

返回一个新的不可变 bytes 数组。

## 概述

bytes 是 bytearray 的不可变序列版本，序列中包含 0～255 范围的整数（1 字节为 8 位，0x00～0xff），拥有索引、切片等不可变序列方法。

## 参数说明

其参数、构造方式与 [[bytearray]] 相同，此外还可以通过字面值创建。

## 示例

```python
c1 = b'\xc4\xe3'  # 字面值创建
# {bytes:2}b'\xc4\xe3'
s1 = c1.decode('gbk')
# {str}'你'
c2 = bytes('你好，中国', encoding='gbk')  # 构造函数创建
# {bytes:10}b'\xc4\xe3\xba\xc3\xa3\xac\xd6\xd0\xb9\xfa'
c3 = bytes(5)
# {bytes:5}b'\x00\x00\x00\x00\x00'

c4 = c2[:4]
# {bytes:4}b'\xc4\xe3\xba\xc3'
s2 = c4.decode('gbk')
# {str}'你好'
c5 = c2 + '！'.encode('gbk')
# {bytes:12}b'\xc4\xe3\xba\xc3\xa3\xac\xd6\xd0\xb9\xfa\xa3\xa1'
s3 = c5.decode('gbk')
# {str}'你好，中国！'
```
