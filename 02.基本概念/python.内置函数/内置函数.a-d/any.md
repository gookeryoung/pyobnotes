---
aliases: 
tags: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 8:57:51 晚上
title: any(iterable)
---

# any(iterable)

如果 iterable 的任一元素为真，则返回 True。如果 iterable 为空或者无一为真，则返回 False。

## 等价代码

```python
def any(iterable):
	for element in iterable:
		if element:
			return True
	return False
```

或者

```python
def any(iterable):
	return True if True in [bool(e) for e in iterable] else False
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

# 查看语数外中是否有超过90分的科目
ch_excellent = [p[0] >= 90 for p in student_scores.values()]
# {list:4}[False, False, False, False]
en_excellent = [p[2] >= 90 for p in student_scores.values()]
# {list:4}[False, False, False, False]
ma_excellent = [p[1] >= 90 for p in student_scores.values()]
# {list:4}[True, True, False, False]
result = [any(cls) for cls in (ch_excellent, en_excellent, ma_excellent)]
# {list:3}[False, False, True]
```
