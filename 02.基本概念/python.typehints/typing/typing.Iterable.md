---
aliases: typing.Iterable,
tags: 
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期四, 十月 13日 2022, 10:44:29 晚上
title: typing.Iterable
---

# typing.Iterable

`typing.Iterable` 通常用于描述 `list`、`tuple`、`set`、`dict` 等一切可迭代对象。

## 示例代码

```Python
# example_typing_Iterable_usage

from typing import Iterable

def greet_all(names: Iterable[str]) -> None:
	for name in names:
		print(f'Hello: {name}')

greet_all(['jack', 'lee', 'martin'])
greet_all(['martin': 'a boy'])
```

```Python
Hello: jack
Hello: lee
Hello: martin
Hello: martin
```
