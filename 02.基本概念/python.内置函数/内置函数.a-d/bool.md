---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:14:13 晚上
title: bool
---

# bool

用标准 [[bool.真值测试]] 进行转换，返回对应布尔值结果。

## 示例

```python
c1, c2 = '', ' '  # 非空内置对象为真
# {str}'', {str}' '
r1, r2 = bool(c1), bool(c2)
# {bool}False, {bool}True

# 内置假常量示例
c3 = [None, False]  # None和False常量
# {list:2}[None, False]
c4 = [0, 0.0, 0j]  # 为0的数值
# {list:3}[0, 0.0, 0j]
c5 = [[], (), {}, set()]  # 空序列或集合
# {list:4}[[], (), {}, set()]
r3 = any([any(c3), any(c4), any(c5)])
# {bool}False
```
