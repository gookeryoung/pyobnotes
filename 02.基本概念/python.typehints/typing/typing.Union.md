---
aliases: typing.Union,
tags: 
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期四, 十月 13日 2022, 10:45:23 晚上
title: typing.Union
---

# typing.Union

`typing.Union` 一般用于描述参数为多个可接受类型中的一种，与 c 语言中的 union 有类似涵义。

其用法如下例：

```Python
# example_typing_union_usage

from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
	if isinstance(user_id, int):
		return f'user-{10000 + user_id}'
	else:
		return user_id

user1 = normalize_id(235)
# {str} 'user-10235'
user2 = normalize_id('u2031')
# {str} 'u2031'
```
