import asyncio


async def fn1(delay,s):
    await asyncio.sleep(delay)
    print(s)

# asyncio.run(fn1(1,'fn1'))
# asyncio.run(fn1(2,'fn2'))
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fn1(1,'fn1'))
        task2 = tg.create_task(fn1(2, 'fn2'))

asyncio.run(main())

