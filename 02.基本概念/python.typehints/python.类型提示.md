---
aliases: python.类型提示, python.typehint
tags: python/类型提示, python/typehint
date created: 星期一, 六月 27日 2022, 8:57:26 早上
date modified: 星期四, 十月 6日 2022, 4:51:00 下午
title: python.类型提示
---

# python.类型提示

2015 年 9 月创始人 Guido van Rossum 在 Python 3.5 引入了一个类型系统，允许开发者指定变量类型。它的主要作用是方便开发，供 IDE 和各种开发工具使用，对代码运行不产生影响，运行时会过滤类型信息。

## 类型提示的优点

了解参数的类型，可以使得理解和维护代码库变得更加容易。例如以下函数：

```Python
def send_request(request_data : Any,
                 headers: Optional[Dict[str, str]],
                 user_id: Optional[UserId] = None,
                 as_json: bool = True):
...
```

只看函数签名，就可以知道以下信息：

- `request_data`：可以是任何类型数据
- `headers`：是一个可选的字典，其 key 和 value 均是字符串
- `user_id`：是一个可选的 UserID 类型，默认为 None
- `as_json`：布尔值，默认为 True

## 如何使用类型提示

### 内置类型提示

以 `str` 为例，在函数中的注解方式如下：

```Python
# example_typehint_str

def greeting(name: str) -> str:
	return f'Hello {name}'
```

该函数接收参数和返回值都是 str 类型，同样的方式也可以应用在 int、float 等各种基础类型上。

### 类型别名

对于操作 tuple、list、dict 等更为复杂的类型时，需要使用到 typing 模块中对应类型别名 Tuple、List、Dict 等，例如：

```Python
# example_typehint_type_aliases
from pathlib import Path
from typing import List, Dict

def get_file_extensions(folders: List[str]) -> Dict[str, List[str]]:  
    file_extensions = {}
    for folder in folders:
	    exts = list(set([f.suffix for f in Path(folder).rglob('*.*')]))
	    file_extensions[Path(folder).stem] = exts
	return file_extensions
```

类型别名还可以用于创建十分复杂的类型，例如：

```Python
# example_typehint_complex_types
from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...
```

等价于以下函数：

```Python
from typing import Tuple, Dict, Sequence

def broadcast_message(
        message: str,
        servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]
) -> None:
    ...
```

### NewType

使用 typing.NewType() 辅助函数可用于创建自定义类型，静态类型检查器会将新类型视为它是原始类型的子类：

```Python
# example_typehint_user_defined

from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
	...

# 静态检查通过
user_a = get_user_name(UserId(42351))

# 静态检查时报错，-1不是 UserId 类型
user_b = get_user_name(-1)

# 返回结果为int
user1 = UserId(23412) + UserId(32102)
# {int} 55514
```

### Callable

对于函数中的回调函数参数，可以使用 `Callable[[Arg1Type, Arg2Type…], ReturnType]`，例如：

```Python
# example_typehint_callable

from typing import Callable

def async_query(on_success: Callable[[int], None],
				on_error: Callable[[int, Exception], None]) -> None:
	...
```
