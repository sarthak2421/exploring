import asyncio
from datetime import datetime


async def fun1():
    # task = asyncio.create_task(fun2())
    print("First..")
    print("Second..")
    await asyncio.sleep(1)
    print("Third..")

async def fun2():
    print("Fourth..")
    await asyncio.sleep(1)
    # await fun1()
    print("Fifth..")

async def main():
    t1 = asyncio.create_task(fun1())
    t2 = asyncio.create_task(fun2())
    await asyncio.gather(t1,t2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

