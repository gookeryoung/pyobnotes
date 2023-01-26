---
aliases: deepcopy深复制, deepcopy
tags: deepcopy
desc: 
date created: 星期五, 十月 7日 2022, 9:56:08 晚上
date modified: 星期四, 一月 26日 2023, 2:38:35 下午
title: deepcopy 深复制
---

# deepcopy 深复制

## 示例代码

```Python
# example_list_copy
lis1 = [3, [55, 44], (7, 8, 9)]
lis2 = lis1 # 引用
lis3 = list(lis1) # 创建副本, 但内部[55, 44]和(7, 8, 9)仍为引用, 下同
lis4 = lis1[:] # 创建副本

lis3[1].append(33)
print(lis4)
# [3, [55, 44, 33], (7, 8, 9)]
```

![[列表浅拷贝.png]]

```Python
# example_deepcopy
import copy

lis1 = [3, [55, 44], (7, 8, 9)]
lis2 = lis1
lis3 = list(lis1)
lis4 = lis1[:]

lis5 = copy.copy(lis1) # 创建副本, 但内部[55, 44]和(7, 8, 9)仍为引用, 同上
lis6 = copy.deepcopy(lis1) # 创建副本, 内部[55, 44]单独拷贝, 但(7, 8, 9)仍为引用, 因为它不可变

lis3[1].append(33)
```

![[列表深拷贝.png]]

### 避免传入可变参数

```Python
class Bus:
    def __init__(self, passengers: list):
        self.passengers = passengers
    def pick(self, person):
        if person not in self.passengers:
            self.passengers.append(person)
        else:
            print(f'{person} already exists!')
    def drop(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
        else:
            print(f'{person} not found!')

basketball_team = 'Jack Lee John Martin'.split()
bus = Bus(basketball_team)
bus.drop('Jack')
bus.drop('Lee')
print(basketball_team)
# {list: 2} ['John', 'Martin']
```

![[列表默认参数示例1.png]]

![[列表默认参数示例2.png]]

应当使用拷贝处理数据, 此处可使用简单的 list 复制即可:

```python
class Bus:
    def __init__(self, passengers: list):
        self.passengers = list(passengers)
    def pick(self, person):
        if person not in self.passengers:
            self.passengers.append(person)
        else:
            print(f'{person} already exists!')
    def drop(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
        else:
            print(f'{person} not found!')

basketball_team = 'Jack Lee John Martin'.split()
bus = Bus(basketball_team)
bus.drop('Jack')
bus.drop('Lee')
print(basketball_team)
# {list: 4} ['Jack', 'Lee', 'John', 'Martin']
```
