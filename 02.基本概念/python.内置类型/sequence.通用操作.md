---
aliases:
tags:
title: sequence.通用操作
date created: 星期四, 三月 2日 2023, 9:14:42 晚上
date modified: 星期四, 三月 2日 2023, 9:21:25 晚上
---

# sequence.通用操作

以下操作对于所有可变与不可变序列均生效:

| 操作                 | 作用                                             |
| -------------------- | ------------------------------------------------ |
| x in s               | 判断元素 x 是否在序列 s 中                       |
| x not in s           | 同上                                             |
| s + t                | 将序列 s 和 t 进行拼接                           |
| s * n                | 将 s 拷贝 n 次                                   |
| s[i]                 | 从 0 开始, s 的第 i + 1 个元素                   |
| s[i:j]               | 从 i 到 j 进行切片, 包含 i … j-1                 |
| len(s)               | 序列 s 的长度                                    |
| min(s)               | s 最小的元素                                     |
| max(s)               | s 最大的元素                                     |
| s.index(x[, i[, j]]) | 元素 x 在序列 s 中首次出现的位置, 在 i 到 j 之间 |
| s.count(x)           | 元素 x 在序列 s 中出现的次数                     |

## 示例

```python
# example_sequence_operations

l1 = list('Hello')
# {list:5} ['H', 'e', 'l', 'l', 'o']
r1 = 'e' in l1
# {bool} True
r2 = '?' not in l1
# {bool} True
l2 = l1 + list(', world!')
# {list:13} ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']
l3 = l1 * 3
# {list: 15} ['H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o']
l4 = l1[1:3]
# {list: 2} ['e', 'l']
n1 = len(l1)
# {int}5
r3, r4 = min(l1), max(l1)
# {str} 'H', {str} 'o'
r5 = l1.count('l')
# {int} 2
```
