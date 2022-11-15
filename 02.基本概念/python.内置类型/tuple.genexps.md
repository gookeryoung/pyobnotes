---
aliases: 生成器表达式, genexps, generator-expression
tags: tuple/genexps, tuple/generator-expression
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 十一月 15日 2022, 10:29:30 晚上
title: tuple.genexps
---

# tuple.genexps

生成器表达式的语法和 [[listcomps列表推导|列表推导]] 差不多，只是将方括号 `[]` 换成圆括号 `()`。

和 [[listcomps列表推导|列表推导]] 不一样的是，采用生成器表达式并不会在内存中生成相应的列表，只会在调用每次 for 循环时生成一个数据。

## 示例代码

```Python
# example_build_tuple_and_array

symbols = '$%^&*(){}[]'
t1 = tuple(ord(s) for s in symbols) # 作为唯一参数时，可以不需要额外括号
# {tuple: 11} (36, 37, 94, 38, 42, 40, 41, 123, 125, 91, 93)
lis1 = list(ord(s) for s in symbols) # 对于list也可以
# {list: 11} [36, 37, 94, 38, 42, 40, 41, 123, 125, 91, 93]

from array import array
arr1 = array('I', (ord(s) for s in symbols)) # 作为非唯一参数，必须有括号
# {array: 11} array('I', [36, 37, 94, 38, 42, 40, 41, 123, 125, 91, 93])
```

```Python
# example_multi_sequence_genexps

colors = ('black', 'white')
# {tulple: 2} ('black', 'white')
sizes = 'S,M,L,XL,XXL'.split(',')
# {list: 5} ['S', 'M', 'L', 'XL', 'XXL']

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
	print(tshirt)
```

输出结果：

```Python
black S
black M
black L
black XL
black XXL
white S
white M
white L
white XL
white XXL
```
