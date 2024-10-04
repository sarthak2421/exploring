import multiprocessing
print(f'Number of CPU: {multiprocessing.cpu_count()}')
import threading
import time

def calc_sq(nums):
    for n in nums:
        print(f'Square of {n} is {n ** 2}')
        # time.sleep(1)

def calc_cube(nums):
    for n in nums:
        print(f'cube of {n} is {n ** 3}')
        # time.sleep(1)

def odd_even(nums):
    for n in nums:
        if n%2==0:
            print(f'{n} is Even')
        else:
            print(f'{n} is Odd')
        # time.sleep(1)

nums = [3,5,7,9,11,13]
nums1 = [1,2,3,4,5,6]

p1 = multiprocessing.Process(target=calc_sq, args=(nums,))
p2 = multiprocessing.Process(target=calc_cube, args=(nums,))
p3 = multiprocessing.Process(target=odd_even, args=(nums1,))
start = time.perf_counter()
p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

end = time.perf_counter()

print(f"Total time:{end-start}")