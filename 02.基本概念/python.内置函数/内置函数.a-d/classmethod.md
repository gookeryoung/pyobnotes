---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:20:09 晚上
title: classmethod/@classmethod
---

# classmethod/@classmethod

将一个方法封装为类方法。

类型: decorator

## 概述

该函数作为 decorator 使用，隐含的第一个参数就是类。一般而言采用以下方案进行定义：

```python
class C:
	@classmethod
	def f(cls, arg1, arg2):...
```

可以直接通过类（如 `C.f()` ）或者具体实例（如 `C().f()` ）进行调用。

## 示例

```python
class C:
	@classmethod
	def f(cls, name, age):
		print(f'name:{name}, age:{age}')

C.f('Jack', 25)
# name:Jack, age:25

c = C()
# {C}<__main__.C object at 0x????????>
c.f('Lee', 30)
# name:Lee, age:30
```
