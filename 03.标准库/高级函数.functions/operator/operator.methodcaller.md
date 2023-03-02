---
aliases: operator.methodcaller, methodcaller
tags: operator/methodcaller
desc: 
date created: Friday, June 24th 2022, 3:16:59 pm
date modified: Wednesday, July 6th 2022, 3:56:37 pm
title: operator.methodcaller
---

# operator.methodcaller

`operator.methodcaller` 可用于在对象上调用指定的方法，如以下示例：

```Python
# example_operator_methodcaller_usage

from operator import methodcaller

upcase = methodcaller('upper')
# {methodcaller} operator.methodcaller('upper')

s = 'The time has come'
# {str} 'The time has come'
r = upcase(s)
# {str} 'THE TIME HAS COME'
```

## 示例代码

可以通过 `operator.methodcaller` 调用打包好的各种方法，如以下例子：

```Python
# example_operator_methodcaller_advanced_usage

from operator import methodcaller

funcs = 'upper lower capitalize title swapcase'.split()
s = 'the TIME has come'

for func in funcs:
	method = methodcaller(func)
	print(f'{func}(\'{s}\') -> {method(s)}')
```

运行结果：

```Python
upper('the TIME has come') -> THE TIME HAS COME
lower('the TIME has come') -> the time has come
capitalize('the TIME has come') -> The time has come
title('the TIME has come') -> The Time Has Come
swapcase('the TIME has come') -> THE time HAS COME
```
