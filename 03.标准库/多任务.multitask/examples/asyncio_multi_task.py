import asyncio


async def coroutine_func(name: str) -> None:
    print(f'开始执行name: {name}')
    await asyncio.sleep(1)
    print(f'执行完成name: {name}')


loop = asyncio.get_event_loop()
tasks = [loop.create_task(coroutine_func(f'test_{str(i)}')) for i in range(3)]
coro = asyncio.wait(tasks)
loop.run_until_complete(coro)

results = [t.result() for t in tasks]
print(results)

loop.close()
