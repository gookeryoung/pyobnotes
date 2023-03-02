---
aliases: functools.lru_cache, lru_cache
tags: functools/lru_cache, lru_cache
desc: 
date created: 星期四, 七月 7日 2022, 8:34:07 晚上
date modified: 星期四, 八月 4日 2022, 10:39:19 晚上
title: functools.lru_cache
---

# functools.lru_cache

`functools.lru_cache` 是一项非常实用的装饰器，它将耗时的函数结果保存起来，避免传入相同参数时的重复计算。

以斐波那契数列函数为例，正常情况下其调用过程如下：

```jupyter
# example_without_lru_cache

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
def fibonacci(n: int):
	return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
	print(f'{"*" * 40} Calling fibonacci(6)')
	fibonacci(6)
```

输出结果：

```Python
[0.00000040]fibonacci(0)->0
[0.00000040]fibonacci(1)->1
[0.00002440]fibonacci(2)->1
[0.00000020]fibonacci(1)->1
[0.00000030]fibonacci(0)->0
[0.00000020]fibonacci(1)->1
[0.00001120]fibonacci(2)->1
[0.00002220]fibonacci(3)->2
[0.00005890]fibonacci(4)->3
[0.00000020]fibonacci(1)->1
[0.00000020]fibonacci(0)->0
[0.00000020]fibonacci(1)->1
[0.00001030]fibonacci(2)->1
[0.00002110]fibonacci(3)->2
[0.00000020]fibonacci(0)->0
[0.00000020]fibonacci(1)->1
[0.00001030]fibonacci(2)->1
[0.00000020]fibonacci(1)->1
[0.00000030]fibonacci(0)->0
[0.00000030]fibonacci(1)->1
[0.00001050]fibonacci(2)->1
[0.00002050]fibonacci(3)->2
[0.00004070]fibonacci(4)->3
[0.00007190]fibonacci(5)->5
[0.00014120]fibonacci(6)->8
```

可以看到过程中反复调用了 `fibonacci(0)`、`fibonacci(1)` 和 `fibonacci(2)`，如果增加两行代码，使用 `functools.lru_cache` 则可以显著改善以上情况：

```Python

# example_with_lru_cache
# ....

from functools import lru_cache

@lru_cache()
@clock
def fibonacci(n: int):
	return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
	print(f'{"*" * 40} Calling fibonacci(6)')
	fibonacci(6)
```

输出结果：

```Python
[0.00000030]fibonacci(0)->0
[0.00000040]fibonacci(1)->1
[0.00002330]fibonacci(2)->1
[0.00000050]fibonacci(3)->2
[0.00003500]fibonacci(4)->3
[0.00000040]fibonacci(5)->5
[0.00004670]fibonacci(6)->8
```

可以看到重复执行的部分被消除了，程序性能得到了改善。以调用 `fibonacci(30)` 为例，不使用 `lru_cache` 需要约 16.17 秒 (AMD 5800H 处理器)，而使用 `lru_cache` 则只需要 0.0002 秒。
