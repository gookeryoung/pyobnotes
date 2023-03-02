---
aliases: functools.singledispatch,
tags: 
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 一月 31日 2023, 9:43:33 晚上
title: functools.singledispatch
---

# functools.singledispatch

## 示例代码

```Python
# example_single_dispatch_usage

import html
import numbers
from collections import abc
from functools import singledispatch

@singledispatch
def htmlize(obj):
	content = html.escape(repr(obj))
	return f'<pre>{content}</pre>'

@htmlize.register(str)
def _(text):
	content = html.escape(text).replace('\n', '<br>\n')
	return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)
def _(n):
	return f'<pre>{n}(0x{n:x})</pre>'

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
	inner = f'</li>\n<li>'.join(htmlize(item) for item in seq)
	return f'<ul>\n<li>{inner}</li>\n</ul>'

s1 = htmlize({1, 2, 3})
# {str} '<pre>{1, 2, 3}</pre>'
s2 = htmlize(abs)
# {str} '<pre>&lt;built-in function abs&gt;</pre>'
s3 = htmlize('Hello, world!\nHello, Python!')
# {str} '<p>Hello, world!<br>\nHello, Python!</p>'
s4 = htmlize(42)
# {str} '<pre>42(0x2a)</pre>'
s5 = htmlize(['alpha', 66, (3, 2, 1)])
# {str} '<ul><li>...</ul>'
```
