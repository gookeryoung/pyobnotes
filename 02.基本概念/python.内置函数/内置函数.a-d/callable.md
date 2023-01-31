---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:18:41 晚上
title: callable(object)
---

# callable(object)

检查参数 `object` 是否可调用，是就返回 `True`，否则返回 `False`。

## 概述

只能判别能否调用，不能用于确认能否调用成功，即如果返回 `True` 也可能调用失败。但如果返回 `False`，则调用肯定不会成功。

注意：在 object 所属类有 `__call__()` 方法的情况下，它也是可调用的。

## 示例

```python
# 可调用类
class Base:
	def __init__(self):...
	def __call__(self):
		print('Class Base is called.')

c1 = Base()
# {Base}<__main__.Base object at 0x????????>
r1 = callable(c1)
# {bool}True

# 可调用函数
r2 = callable(print)
# {bool}True
```
