---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:08:37 晚上
title: bin
---

# bin

将整数转为以 `0b` 为前缀的二进制字符串。如果不是整数对象，则必须定义 `__index__()` 方法。

## 示例

```python
s1 = bin(3)
# {str}'0b11'
s2 = bin(-10)
# {str}'-0b1010'
lis = [e for e in s2]
# {list:7}['-', '0', 'b', '1', '0', '1', '0']
```
