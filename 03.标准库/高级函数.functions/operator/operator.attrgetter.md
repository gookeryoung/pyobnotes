---
aliases: operator.attrgetter, attrgetter
tags: operator/attrgetter
desc: 过名称提取对象的属性，类似于使用 `.` 运算符。
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期四, 三月 2日 2023, 8:30:11 晚上
title: operator.attrgetter
---

# operator.attrgetter

`attrgetter` 支持通过名称提取对象的属性，类似于使用 `.` 运算符，其基本用法如下：

```jupyter
# example_operator_attrgetter_usage

from collections import namedtuple
from operator import attrgetter

Score = namedtuple('Score', 'chinese math english')
StudentScore = namedtuple('StudentScore', 'name age score')

score_data = [
	('Jack', 18, (90, 125, 117)),
	('Lee', 17, (121, 115, 109)),
	('Wang', 18, (119, 97, 120))
]
student_scores = [StudentScore(n, a, Score(*s)) for n, a, s in score_data]

print('Sort by math score:')
for score in sorted(student_scores, key=attrgetter('score.math')):
	print(score)
```
