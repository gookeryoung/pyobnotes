---
aliases: Python.threading
tags: threading
date created: 星期日, 六月 26日 2022, 12:21:24 中午
date modified: 星期三, 九月 7日 2022, 12:20:04 中午
title: threading.基本概念
---

# threading.基本概念

## 概述

在 Python 中，多线程最常见的一个场景就是爬虫，例如这样一个需求，有多个结构一样的页面需要爬取，例如下方的 URL（豆瓣阿凡达影评，以 10 个为例）：

```Python
```text
url_list = [
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=0',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=20',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=40',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=60',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=80',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=100',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=120',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=140',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=160',
      'https://movie.douban.com/subject/1652587/reviews?sort=time&start=180'
]
```

如果依次爬取，请求第一个页面 ->得到返回数据 ->解析数据 ->提取、存储数据 ->请求第二个页面，按照这样的思路，那么**大量时间都会浪费在请求、返回数据上**，如果**在等待第一个页面返回数据时去请求第二个页面**，就能有效的提高效率，多线程就可以实现这样的功能。

## 多线程概念

先从一个简单的例子开始，定义 process() 函数，执行该函数需要消耗 1 秒。

```Python
import time

def process():
	print('Start thread.')
	time.sleep(1)
	print('End thread.')

def main():
	start = time.perf_counter()
	process()
	print(f'Time used: {time.perf_counter() - start:.2f} seconds.')

if __name__ == '__main__':
	main()
```

得到的结果是：

```Python
Start thread.
End thread.
Time used: 1.00 seconds.
```

如果将两个过程 `process()` 进行叠加：

```Python
import time

def process():
	print('Start thread.')
	time.sleep(1)
	print('End thread.')

def main():
	start = time.perf_counter()
	process()
	process()
	print(f'Time used: {time.perf_counter() - start:.2f} seconds.')

if __name__ == '__main__':
	main()
```

得到结果也会是两个 process() 时间的叠加：

```Python
Start thread.
End thread.
Start thread.
End thread.
Time used: 2.01 seconds.
```

这就是常见的串行程序的思路，CPU 在执行第一个函数中，等待 1 秒的时间里什么也不做，在执行完第一个函数后接着执行第二个函数。其执行过程如下：

![[threading_example_single]]

很明显，这样让 CPU 干等着啥也不做并不是一个很好的选择，而**多线程**就是解决这一问题的方法之一，**让 CPU 在等待某个任务完成时去执行更多的操作**，将整个过程简化为下图流程，这样就能充分节省时间：

![[threading_example_multi]]

## threading 基本使用

使用 threading 通过多线程的方式实现上面的过程，只需要定义两个线程并依次启动即可：

```Python
import time
import threading

def process():
	print('Start thread.')
	time.sleep(1)
	print('End thread.')

def main():
	start = time.perf_counter()
	t1 = threading.Thread(target=process)
	t2 = threading.Thread(target=process)
	t1.start()
	t2.start()
	print(f'Time used: {time.perf_counter() - start:.2f} seconds.')

if __name__ == '__main__':
	main()
```

执行上述代码结果如下：

```Python
Start thread.
Start thread.Time used: 0.00 seconds.
End thread.End thread.
```

可以看到，两个子线程确实同时启动，但是**主线程并未等待两个子线程执行完毕就直接结束**，所以总时间为 0。

为了解决这个问题，我们可以使用 threading.join() 方法，意思是在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

换成人话就是**让主线程挂起，等待所有子线程结束再执行**，体现到代码上也很简单，只需要添加两行即可：

```Python
import time
import threading

def process():
	print('Start thread.')
	time.sleep(1)
	print('End thread.')

def main():
	start = time.perf_counter()
	t1 = threading.Thread(target=process)
	t2 = threading.Thread(target=process)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(f'Time used: {time.perf_counter() - start:.2f} seconds.')

if __name__ == '__main__':
	main()
```

运行结果如下，全部代码在 1 秒内运行完毕：

```Python
Start thread.
Start thread.
End thread.End thread.
Time used: 1.00 seconds.
```

至此，我们得到了第一个有效的多线程代码，也能大致理解 threading 的基本使用流程。
