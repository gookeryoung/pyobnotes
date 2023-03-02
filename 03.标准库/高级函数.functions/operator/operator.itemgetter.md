---
aliases: operator.itemgetter, itemgetter
tags: operator/itemgetter
desc: 生成从序列中取出特定位置元素的方法。
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Wednesday, July 6th 2022, 3:09:23 pm
title: operator.itemgetter
---

# operator.itemgetter

`itemgetter` 支持从序列中取出特定位置的元素，同时不需要使用 `lambda` 匿名函数，类似于使用 `[]` 运算符，能够支持任何已实现 `__getitem__` 方法的类，其基本用法如下：

```Python
# example_itemgetter_usage

from operator import itemgetter

# name, age, chinese, math, english
student_scores = [
	('Jack', 18, 90, 125, 117),
	('Lee', 17, 121, 115, 109),
	('Wang', 18, 119, 97, 120)
]

get_score = itemgetter(2, 3, 4)
for stu in student_scores:
	print(get_score(stu))
```

运行结果：

```Python
(90, 125, 117)
(121, 115, 109)
(119, 97, 120)
```

## 示例代码

`itemgetter` 最常见的用法是根据元组某个字段进行排序，例如：

```Python
# example_itemgetter

from collections import namedtuple
from operator import itemgetter

LatLong = namedtuple('LatLong', 'Lat Long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_data = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
]
metro_areas = [Metropolis(n, c, p, co) for n, c, p, co in metro_data]

# sort by country
print('Sort by country:')
for area in sorted(metro_areas, key=itemgetter(1)):
	print(area)

# sort by population
print('\nSort by population:')
for area in sorted(metro_areas, key=itemgetter(2)):
	print(area)
```

运行结果：

```Python
Sort by country:
Metropolis(name='Delhi NCR', cc='IN', pop=21.935, coord=(28.613, 77.208889))
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=(35.689722, 139.691667))
Metropolis(name='Mexico City', cc='MX', pop=20.142, coord=(19.43333, -99.133333))
Metropolis(name='New York-Newark', cc='US', pop=20.104, coord=(40.808611, -74.020386))
Sort by population:
Metropolis(name='New York-Newark', cc='US', pop=20.104, coord=(40.808611, -74.020386))
Metropolis(name='Mexico City', cc='MX', pop=20.142, coord=(19.43333, -99.133333))
Metropolis(name='Delhi NCR', cc='IN', pop=21.935, coord=(28.613, 77.208889))
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=(35.689722, 139.691667))
```
