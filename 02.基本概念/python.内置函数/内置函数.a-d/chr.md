---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:19:53 晚上
title: chr(i)
---

# chr(i)

返回 Unicode 码位整数 i 对应的字符串格式。

## 概述

可接受的参数 `i` 的范围是 0～0x10FFFF（Unicode 最大范围）。

## 示例

```python
c1 = chr(0)
# {str}'\x00'
c2 = ''.join([chr(x) for x in range(65, 65+26)])
# {str}'ABC...Z', 大写字母
c3, c4 = chr(97), chr(97+25)  # 小写字母
# {str}'a', {str}'z'
c5 = chr(20320)  # 中文字符
# {str}'你'
```
