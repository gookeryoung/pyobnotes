---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 8:57:43 晚上
title: all(iterable)
---

# all(iterable)

如果 iterable 的所有元素为真，则返回 True。

## 等价代码

```python
def all(iterable):
	for element in iterable:
		if not element:
			return False
	return True
```

或者

```python
def all(iterable):
	return True if False not in [bool(e) for e in iterable] else False
```

## 示例

```python
student_scores = {
    # 名字: 语文，数学，英语
    'Huang': (80, 90, 64),
    'Lee': (58, 94, 60),
    'Chen': (88, 75, 78),
    'Chow': (65, 72, 82)
}

# 查看语数外中是否有不及格的科目, False为不及格
ch_pass = [p[0] >= 60 for p in student_scores.values()]
# {list:4}[True, False, True, True]
en_pass = [p[2] >= 60 for p in student_scores.values()]
# {list:4}[True, True, True, True]
ma_pass = [p[1] >= 60 for p in student_scores.values()]
# {list:4}[True, True, True, True]
result = [all(cls) for cls in (ch_pass, en_pass, ma_pass)]
# {list:3}[False, True, True]
```
