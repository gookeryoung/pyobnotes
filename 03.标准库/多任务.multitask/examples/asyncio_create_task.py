import asyncio


async def coroutine_func():
    """暂停1秒后输出 end coroutine function"""
    print('start...')
    await asyncio.sleep(1)
    print('end coroutine function')


coro = coroutine_func()
loop = asyncio.get_event_loop()
task = loop.create_task(coro)
print(f'status: {task}\n')

loop.run_until_complete(task)
print(f'status: {task}\n')
loop.close()
