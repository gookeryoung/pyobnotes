---
aliases: tuple, 元组
tags: tuple, 元组
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 十一月 15日 2022, 10:26:28 晚上
title: Tuple 元组
desc: 元组（tuple）是 Python 中另一个重要的序列结构，和列表类似，元组也是由一系列按特定顺序排序的元素组成。
---

# Tuple 元组

元组（tuple）是 Python 中另一个重要的序列结构，和列表类似，元组也是由一系列按特定顺序排序的元素组成。

元组和列表（list）的不同之处在于：

- 列表 list 的元素是可以更改的，包括修改值，删除和插入元素，所以列表是可变序列；
- 而元组 tuple 一旦被创建，它的元素就不可更改了，所以元组是不可变序列。

## 示例代码

```python
import os

filepath = r'd:\designtools\sample\config.txt'
# {str} 'd:\\designtools\\sample\\config.txt'
_, filename = os.path.split(filepath)
# {str} 'config.txt'
```
