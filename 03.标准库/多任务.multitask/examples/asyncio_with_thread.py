import asyncio
from threading import Thread


def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def thread_example(name):
    print(f'开始执行name: {name}')
    await asyncio.sleep(1)
    print(f'执行完成name: {name}')


my_loop = asyncio.new_event_loop()
t = Thread(target=start_thread_loop, args=(my_loop,))
t.start()

for i in range(3):
    future = asyncio.run_coroutine_threadsafe(thread_example(f'test_{str(i)}'), my_loop)
    print(future.result())

print('主线程未受影响')

for i in range(4, 7):
    future = asyncio.run_coroutine_threadsafe(thread_example(f'test_{str(i)}'), my_loop)
    print(future.result())

print('主线程继续')
