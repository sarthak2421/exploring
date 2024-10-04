import asyncio

async def fn1(delay,s):
    await asyncio.sleep(delay)
    print(s)

# asyncio.run(fn1(1,'fn1'))
# asyncio.run(fn1(2,'fn2'))
async def main():
    task1 = asyncio.create_task(fn1(1,'fn1'))
    task2 = asyncio.create_task(fn1(2, 'fn2'))
    await task1
    await task2
asyncio.run(main())
