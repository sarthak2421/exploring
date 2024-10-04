import asyncio

async def fun1():
    # task = asyncio.create_task(fun2())
    print("First..")
    # await fun2()
    # await asyncio.sleep(1)
    print("Second..")
    await asyncio.sleep(1)
    print("Third..")

async def fun2():
    print("Fourth..")
    await asyncio.sleep(1)
    # await fun1()
    print("Fifth..")


async def main():
    await asyncio.gather(
        fun1(),
        fun2()
    )

asyncio.run(main())