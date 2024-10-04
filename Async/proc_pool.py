import multiprocessing
import os

def test(num):
    print(f'PID for {num} is {os.getpid()}')

pool = multiprocessing.Pool(4)
processes = [pool.apply_async(test,(x,)) for x in range(1,11)]
res = [p.get() for p in processes]
# print(res)

