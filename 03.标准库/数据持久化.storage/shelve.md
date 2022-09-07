---
aliases: shelve,
tags: shelve
desc: 
date created: 星期四, 八月 18日 2022, 9:51:38 晚上
date modified: 星期三, 九月 7日 2022, 1:22:10 下午
title: shelve
---

# shelve

`shelve` 模块用于**任意 python 对象**的持久化存储，并采用字典形式的 API，相当于 [[pickle]] 模块的升级简化版。

其数据采用 [[dbm|dbm]] 模块进行管理，但使用者无需接触数据库底层代码。

## 基本使用

```python
# example_shelve_read_write

from array import array
from random import randint
import shelve

with shelve.open('test_shelve.db') as s:
	s['sample_key'] = {'num1': 10, 'num2': 9.5, 'str_name': 'jack lee'}
	s['obj_key'] = array('i', [randint(0, 100) for _ in range(50)])
	# s: <shelve.DbfilenameShelf object at 0x06CD4418>

with shelve.open('test_shelve.db', flag='r') as s:
	data = s['sample_key']
	# data_read: {'num1': 10, 'num2': 9.5, 'str_name': 'jack lee'}

	numbers = s['obj_key']
	# numbers: {array: 50} array('i', [76, 98, 53, ...])
```
