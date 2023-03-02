---
aliases: threading.线程池
tags: 
title: threading.线程池
date created: 星期二, 十月 4日 2022, 10:07:18 晚上
date modified: 星期四, 三月 2日 2023, 7:39:11 晚上
---

# threading.线程池

## 概述

系统启动一个新线程的成本较高，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以提升性能，尤其是当程序中需要创建大量生存期很短的线程时，则更应该考虑使用线程池。

线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。

此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致 Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

## 线程池使用

线程池的基类是 `concurrent.futures` 模块中的 `Executor`，`Executor` 提供了两个子类，即 `ThreadPoolExecutor` 和 `ProcessPoolExecutor`，其中 `ThreadPoolExecutor` 用于创建线程池，而 `ProcessPoolExecutor` 用于创建进程池。

使用线程池来执行线程任务的步骤如下：

- 调用 `ThreadPoolExecutor` 类的构造器创建一个线程池；
- 定义一个普通函数作为线程任务；
- 调用 `ThreadPoolExecutor` 对象的 `submit()` 方法 或者 `map()` 方法来提交线程任务；
- 当不想提交任何任务时，调用 `ThreadPoolExecutor` 对象的 `shutdown()` 方法来关闭线程池。如果使用 `with` 上下文创建线程池对象，则不需要手动调用 `shutdown()` 进行关闭。

以下为使用线程池进行多 url 下载的示例：

```python
# example_threadpool_download

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen  
  
def load_url(url: str, timeout: int = 60) -> str:  
    with urlopen(url, timeout=timeout) as conn:  
        return conn.read()
 
if __name__ == '__main__':
    urls = (  
        'https://www.baidu.com/',  
        'https://www.huawei.com/',  
        'https://www.taobao.com/',  
        'https://www.jd.com/',  
        'https://www.163.com/',  
    )  
  
    with ThreadPoolExecutor(max_workers=5) as executor:  
        results = executor.map(load_url, urls)  
  
    for r in results:
        print(len(BeautifulSoup(r, features='lxml').text))
```
