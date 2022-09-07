---
aliases: time.perf_counter
tags: time.perf_counter
date created: 星期四, 六月 23日 2022, 9:49:29 晚上
date modified: 星期三, 九月 7日 2022, 1:19:34 下午
title: perf_counter
---

# perf_counter

> 类型：function
> 说明：返回一个性能计数器的浮点值（单位为秒），即用于测量较短持续时间的具有最高有效精度的时钟。 它会包括睡眠状态所消耗的时间并且作用于全系统范围。 返回值的参考点未被定义，因此只有两次调用之间的差值才是有效的。

## 示例代码

```python
from array import array
from random import random
from time import perf_counter as pc
from time import perf_counter_ns as pcn

def operate_float_array(size: int) -> None:
	floats = array('f', (random() for i in range(size + 1)))
	with open('floats_array.bin', 'wb') as f:
		f.write(floats)
	floats_read = array('f')
	with open('floats_array.bin', 'rb') as f:
		floats_read.fromfile(f, size + 1)
	print(floats_read[-5:])

# 使用 perf_counter 计算用时，单位：秒
t0 = pc()
operate_float_array(10000000)
print(f'Time used:\t{(pc() - t0):.3f}s')

# 使用 perf_counter_ns 计算用时，单位：纳秒
t1 = pcn()
operate_float_array(10000000)
print(f'Time used:\t{(pcn() - t1):.3f}ns')
```
