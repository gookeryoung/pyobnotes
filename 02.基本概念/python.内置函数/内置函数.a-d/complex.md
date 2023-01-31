---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:26:38 晚上
title: 'complex([real[, image]])'
---

# complex([real[, image]])

返回值为 real + image * 1j 的复数，或者将字符串或数字转化为复数。

## 概述

根据参数的不同，其转化规则如下：

- 如果第一个参数为数值，且无第二个参数则默认虚部为零。两个参数均省略则默认为 `0j` ；
- 如果第一个参数为字符串，则其被转换为复数，此时不能有第二个参数；
- 如果为普通对象，则会调用内部方法 `complex()` ， 如果未定义则退回调用 `float()` ，如果未定义则退回调用 `index()`。

## 示例

```python
c1 = complex(1, 2)
# {complex}(1+2j)
c2 = complex(1)
# {complex}(1+0j)
c3 = complex()
# {complex}(0j)
c4 = complex('2-5j')
# {complex}(2-5j)

class C:
	def __init__(self, x):
		self.x = x
	def __complex__(self):
		return complex(self.x, self.x * 2)

c5 = complex(C(3))
# {complex}(3+6j)
```
