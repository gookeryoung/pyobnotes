---
aliases: string,
tags: 
desc: 
date created: 星期日, 八月 7日 2022, 4:12:11 下午
date modified: 星期日, 八月 7日 2022, 5:48:08 下午
title: string
---

# string

`string` 模块可追溯至早期的 python 版本，该模块中大部分函数均已在 `str` 对象中实现，在 `string` 模块中只保留了部分有用的常数和类，用于处理 `str` 对象。

## string.constants

`string` 模块包含了一系列 `ascii` 和数字字符相关常量，包括：

```python
import string

string_constants = {
	'ascii_letters': string.ascii_letters,
	'ascii_lowercase': string.ascii_lowercase,
	'ascii_uppercase': string.ascii_uppercase,
	'digits': string.digits,
	'hexdigits': string.hexdigits,
	'octdigits': string.octdigits,
	'printable': string.printable,
	'punctuation': string.punctuation,
	'whitespace': string.whitespace
}

for name, value in string_constants.items():
	print('%s=%r' % (name, value))
```

```python
ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
hexdigits='0123456789abcdefABCDEF'
octdigits='01234567'
printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace=' \t\n\r\x0b\x0c'
```

## string.functions

目前只有一个 `capwords` 函数可供使用。

### capwords

将字符串所有单词大写后返回新字符串，等价于：

```python
def capwords(s: str):
	return ' '.join([x.capitalize() for x in s.split(' ')])
```

使用示例：

```python
# example_string_capwords

import string

print(string.capwords('hello, tomas young!'))
# Hello, Tomas Young!
```

## string.Template

`string.Template` 主要用于实现文本的模板替代，默认使用 `$` 作为标识符（例如 `$var`）。当存在周围文本时，则需要使用 `${var}` 格式。

```python
# example_string_template

import string

t = string.Template("""
系统名称:\t$system_name
开发作者:\t$author
简述:\t\t${system_name}是由${author}开发的一套系统。
""")

values = {
	'system_name': 'Automatic Driver System',
	'author': 'Tomas J.C.'
}

print(t.substitute(values))
```

```python
系统名称:       Automatic Driver System
开发作者:       Tomas J.C.
简述:           Automatic Driver System是由Tomas J.C.开发的一套系统。
```

也可以使用 `%` 操作符或者 `str.format` 实现等同功能：

```python
#example_%_template

s = """
系统名称:\t%(system_name)s
开发作者:\t%(author)s
简述:\t\t%(system_name)s是由%(author)s开发的一套系统。
"""

values = {
	'system_name': 'Automatic Driver System',
	'author': 'Tomas J.C.'
}

print(s % values)
```

```python
# example_format_template

s = """
系统名称:\t{system_name}
开发作者:\t{author}
简述:\t\t{system_name}是由{author}开发的一套系统。
"""

print(s.format(system_name='Automatic Driver System', author='Tomas J.C.'))
```

## string.Template 继承

可以通过继承 `string.Template` 的方式自定义字符串模板替代方法，只需要改变其 `delimiter` 和 `idpattern` 属性即可。

```python
# example_advanced_template

import string

class MyTemplate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'

t = """
author:\t\t\t%{author}
author_:\t\t%{author_}
author_s:\t\t%{author_s}
author_under:\t%{author_under}
"""

values = {
	'author': 'jack',
	'author_': 'jack_',
	'author_s': 'jack_s',
	'author_under': 'jack_under'
}

mt = MyTemplate(t)
print(mt.safe_substitute(values))
```

```python
author:			%{author}
author_:		%{author_}
author_s:		jack_s
author_under:	jack_under
```
