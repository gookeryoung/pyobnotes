---
aliases: functools.partial, partial
tags: functools/partial
desc: 将原函数某些参数固定，返回一个新的可调用对象。
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:43:30 晚上
title: functools.partial
---

# functools.partial

`functools.partial` 是一个高阶函数，用于部分应用一个函数。`部分应用` 是指将原函数某些参数固定，返回一个新的可调用对象。可以用这种方法实现把接受一个或多个参数的函数改变成需要回调的 API，如以下示例：

```Python
# example_functools_partial_usage

from functools import partial
from operator import mul
from time import strftime

# one arg function
cur_time = partial(strftime, '%Y%m%d-%H%M%S')
# {partial} functools.partial(<built-in function strftime>, '%Y%m%d-%H%M%S')
r1 = cur_time()
# {str} '20220706-161127'

# two args' function
triple = partial(mul, 3)
# {partial} functools.partial(<built-in function mul>, 3)
r2 = [triple(x) for x in range(1, 10)]
# {list: 9} [3, 6, 9, 12, 15, 18, 21, 24, 27]
```
