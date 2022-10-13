---
aliases: typing.TypeVar,
tags: 
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期四, 十月 13日 2022, 10:45:27 晚上
title: typing.TypeVar
---

# typing.TypeVar

`typing.TypeVar` 是用于处理泛型定义的，在知道目标可选类型时较 `typing.Any` 更好。

## 示例代码

```Python
# example_typing_typevar

from typing import TypeVar, List

Numbers = TypeVar('Numbers', int, float, List[int], List[float])

def add(left: Numbers, right: Numbers) -> Numbers:
	if isinstance(left, List):
		return [left[i] + right[i] for i in range(len(left))]
	return left + right

r1 = add(1, 2)
# {int} 3
r2 = add(1.0, 2.0)
# {float} 3
r3 = add([1, 2], [3, 4])
# {list:2} [4, 6]
r4 = add([1.0, 2.0], [3.0, 4.0])
# {list:2} [4.0, 6.0]
```
