---
aliases: shelve,
tags: shelve
desc: 
date created: 星期四, 八月 18日 2022, 9:51:38 晚上
date modified: 星期四, 八月 18日 2022, 10:15:46 晚上
title: shelve
---

# shelve

`shelve` 模块用于任意 python 对象的持久化存储，并采用字典形式的 API，相当于 [[pickle]] 模块的升级简化版。

其数据采用 [[dbm]] 模块进行管理，但使用者无需接触数据库底层代码。

## 数据写入与读取

```python
# example_shelve_read_write

import shelve

with shelve.open('test_shelve.db') as s:
	s['sample_key'] = {'num1': 10, 'num2': 9.5, 'str_name': 'jack lee'}
	# s: <shelve.DbfilenameShelf object at 0x06CD4418>

with shelve.open('test_shelve.db', flag='r') as s:
	data_read = s['sample_key']
	# data_read: {'num1': 10, 'num2': 9.5, 'str_name': 'jack lee'}

print(data_read['str_name'])
```

```python
jack lee
```
