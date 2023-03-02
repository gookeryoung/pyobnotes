---
aliases: operator.mul, mul
tags: operator/mul
desc: 提供乘法运算符函数，表示两个元素之乘积。
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Wednesday, July 6th 2022, 3:03:35 pm
title: operator.mul
---

# operator.mul

提供乘法运算符函数，表示两个元素之乘积，避免写匿名函数 `lambda a, b: a *b`。

以下为使用 `operator.mul` 实现的阶乘函数：

```Python
# example_operator_mul

from functools import reduce
from operator import mul

def fact(n: int):
	return reduce(mul, range(1, n + 1))

r1 = fact(5)
# {int} 120
r2 = fact(8)
# {int} 40320
r3 = fact(10)
# {int} 3628800
```
