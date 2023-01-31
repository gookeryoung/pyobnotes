---
aliases: functools.wraps, wraps
tags: functools/wraps
desc: 
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Thursday, July 7th 2022, 8:40:34 pm
title: functools.wraps
---

# functools.wraps

## 示例代码

`functools.wraps` 主要用于协助构建运行良好的装饰器，能够正确地处理关键字参数并复制原函数的各项属性。

```Python
# example_functools_wraps_usage

from functools import wraps
from time import perf_counter, sleep

def clock(func):
	@wraps(func)
	def clocked(*args, **kwargs):
		t0 = perf_counter()
		result = func(*args, **kwargs)
		elapsed = perf_counter() - t0
		name = func.__name__
		arg_lst = []
		if args:
			arg_lst.append(', '.join(repr(arg) for arg in args))
		if kwargs:
			pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
			arg_lst.append(', '.join(pairs))
		arg_str = ', '.join(arg_lst) 
		print(f'[{elapsed:0.8f}]{name}({arg_str})->{result}')
		return result
	return clocked


@clock
def snooze(seconds: int) -> None:
	sleep(seconds)

@clock
def factorial(n: int):
	return 1 if n < 2 else n * factorial(n - 1)

if __name__ == '__main__':
	print(f'{"*" * 40} Calling snooze(2)')
	snooze(2)
	print(f'{"*" * 40} Calling factorial(6)')
	factorial(6)
```
