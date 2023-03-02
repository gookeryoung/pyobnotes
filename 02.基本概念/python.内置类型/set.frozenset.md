---
aliases: 
tags: 
title: set.frozenset
date created: 星期四, 三月 2日 2023, 9:03:08 晚上
date modified: 星期四, 三月 2日 2023, 9:12:35 晚上
---

# set.frozenset

一个冻结的集合，不能再添加或删除任何元素。

## 示例代码

```python
# example_frozenset

f1 = frozenset(range(10))
# {frozenset: 10} frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
f2 = frozenset('foo bar')
# {frozenset:6} frozenset({'f', 'o', 'b', 'a', 'r', ' '})

f3 = f1.intersection(int(_) for _ in '123')
# {frozenset:3} frozenset({1, 2, 3})
```
