---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:27:15 晚上
title: 'delattr(object, name)'
---

# delattr(object, name)

`setattr()` 相关函数，在目标对象允许的情况下删除指定属性。

## 示例

```python
class C:
	def __init__(self, name):
		self.name = name
	def say(self):
		if 'name' in dir(self):
			return f'My name is {self.name}.'
		else:
			return 'I forgot my name.'

c = C('Jack')
# {C}<__main__.C object at 0x????????>
b1 = 'name' in dir(c)
# {bool}True
r1 = c.say()
# My name is Jack.

delattr(c, 'name')
b2 = 'name' in dir(c)
# {bool}False
r2 = c.say()
# I forgot my name.
```
