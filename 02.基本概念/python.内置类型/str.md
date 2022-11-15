---
aliases: 字符串,
tags: 
desc: 
date created: 星期五, 十月 7日 2022, 9:56:06 晚上
date modified: 星期二, 十一月 15日 2022, 10:30:56 晚上
title: str
---

# str

## 示例代码

```Python
# example_str_unicodes

s1 = '你好'
# {str: 2} '你好'
b1 = s1.encode('utf-8')
# {bytes: 6} b'\xe4\xbd\xa0\xe5\xa5\xbd'
s2 = (b1 + b',\xe4\xb8\xad\xe5\x9b\xbd').decode('utf-8')
# {str: 5} '你好,中国'
```

可以使用各种字符串方法处理 `bytes` 二进制序列，例如 `endswith`, `replace`, `upper` 等。

```Python
# example_bytes_functions

b1 = 'hello,china.你好,中国'.encode('utf8')
# {bytes: 25} b'hello,china.\xe4\xbd\xa0\xe5\xa5\xbd,\xe4\xb8\xad\xe5\x9b\xbd'
r1 = b1.endswith('国'.encode('utf8'))
# {bool} True
s1 = b1.upper().decode('utf8')
# {str} 'HELLO,CHINA.你好,中国'
s2 = b1.decode('utf8').upper()
# {str} 'HELLO,CHINA.你好,中国'
```
