---
aliases: set集合,
tags: 
desc:  
date created: 星期五, 十月 7日 2022, 9:56:08 晚上
date modified: 星期四, 三月 2日 2023, 9:03:00 晚上
title: set.set
---

# set.set

通过 `iterable` 序列创建一个集合, 其元素是**不重复**且 `hashable` 的。

通常用于元素包含测试。

## 示例代码

### 集合创建

```Python
# example_set_creation

s1 = {'spam', 'foo', 'foo', 'spam'}
# {set: 2} {'foo', 'spam'}
s2 = set('abcbarbcraac')
# {set: 4} {'b', 'c', 'a', 'r'} 
s3 = {e for e in 'hello'}
# {set: 4} {'h', 'l', 'e', 'o'}
```

## 集合操作

```Python
# example_set_operations

r1 = len(set('hello'))
# {int} 4
s1 = {e for e in 'hello'}
s2 = {e for e in 'hello, world!'}
s3 = {e for e in 'Hello'}
r2 = 'h' in s1 # 元素'h'是否在集合s1内
# {bool} True

r3 = s1 <= s2 # 集合s1是否为s2子集
# {bool} True

r4 = set('abc').isdisjoint('efc') # 集合是否与其他集合无交集
# {bool} False
r5 = set('abc').isdisjoint('def')
# {bool} True

s4 = set('abc').union('def') # 求并集
# {set: 6} {'a', 'b', 'c', 'd', 'e', 'f'}
s5 = set('abc').intersection('dec') # 求交集
# {set: 1} {'c'}
```
