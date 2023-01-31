---
aliases: [内置函数/abs(x)]
tags: [abs]
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 8:57:09 晚上
title: abs(x)
---

# abs(x)

返回一个数的绝对值，参数 x 可以是整数、浮点数或实现了 `__abs__()` 的对象。

## 示例代码

```python
numbers = [12, -11, 3.0, -2.15]
ret = [abs(n) for n in numbers]
# {list: 4} [12, 11, 3.0, 2.15]
```
