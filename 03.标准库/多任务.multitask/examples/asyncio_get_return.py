import asyncio


async def coroutine_func():
    """暂停1秒后输出 end coroutine function"""
    print('start...')
    await asyncio.sleep(1)
    print('end coroutine function')


# 方法1：通过task.result()获取返回值
coro = coroutine_func()
loop = asyncio.get_event_loop()
task = loop.create_task(coro)
print(f'status: {task}\n')
try:
    print(f'return value: {task.result()}')
except asyncio.InvalidStateError:
    print('task is not finished yet.')

loop.run_until_complete(task)
print(f'status: {task}\n')
print(f'return value: {task.result()}')


# 方法2：通过add_done_callback()获取返回值
def my_callback(future):
    print(f'return value by callback: {future.result}')


coro2 = coroutine_func()
task2 = loop.create_task(coro2)
task2.add_done_callback(my_callback)
loop.run_until_complete(task2)

loop.close()
