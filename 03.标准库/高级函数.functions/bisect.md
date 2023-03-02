---
aliases: bisect
tags: bisect
desc: 
date created: 星期五, 十月 7日 2022, 9:56:08 晚上
date modified: 星期四, 三月 2日 2023, 8:07:56 晚上
title: bisect
---

# bisect

这个模块对有序列表提供了支持，使得他们可以在插入新数据仍然保持有序。

主要包含两个函数：

 - `bisect.bisect()` 用于进行二分查找,不会影响到源序列;
 - `bisect.insort()` 用于进行二分插入, 会改变源序列。

## 示例代码

```Python
# example_bisect_bisect

from bisect import bisect

def grade(score: int):
	breakpoints = tuple(range(60, 100, 10))
	grades = 'FDCBA'
	i = bisect(breakpoints, score)
	return grades[i]

r1 = grade(63)
# {str} 'D'
r2 = [grade(x) for x in (55, 75, 82, 63, 91, 100)]
# {list: 6} ['F', 'C', 'B', 'D', 'A', 'A']
```

排序很耗时，在得到一个有序序列以后，最好能够保持其处于有序状态，而 `bisect.insort` 即是如此。

`insort(seq, item)` 可以将变量 `item` 插入到序列 `seq` 中，并保持其处于升序状态，例如：

```Python
# example_bisect_insort

from bisect import insort
from random import randrange, seed

SIZE = 7
seed(1729)

lis = []
for i in range(SIZE):
	item = randrange(SIZE * 2)
	insort(lis, item)
	print(f'{item:2d} -> {lis}')
```

输出结果为：

```Python
10 -> [10]
 0 -> [0, 10]
 6 -> [0, 6, 10]
 8 -> [0, 6, 8, 10]
 7 -> [0, 6, 7, 8, 10]
 2 -> [0, 2, 6, 7, 8, 10]
10 -> [0, 2, 6, 7, 8, 10, 10]
```

## 性能说明

当使用 `bisect()` 和 `insort()` 编写时间敏感的代码时，请记住以下概念。

- 二分法对于搜索一定范围的值是很高效的。 对于定位特定的值，则字典的性能更好。
- `insort()` 函数的时间复杂度为 `O(n)`, 因为对数时间的搜索步骤被线性时间的插入步骤所主导。
- 这些搜索函数都是无状态的并且会在它们被使用后丢弃键函数的结果。 因此，如果在一个循环中使用搜索函数，则键函数可能会在同一个数据元素上被反复调用。
- 如果键函数速度不快，请考虑用 [`functools.cache()`](https://docs.python.org/zh-cn/3/library/functools.html#functools.cache "functools.cache") 来包装它以避免重复计算。 另外，也可以考虑搜索一个预先计算好的键数组来定位插入点（如下面的示例节所演示的）。
