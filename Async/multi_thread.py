import threading
import time

def calc_sq(nums):
    for n in nums:
        print(f'Square of {n} is {n ** 2}')
        # time.sleep(1)

def calc_cube(nums):
    for n in nums:
        print(f'cube of {n} is {n ** 3}')
#         time.sleep(1)

def odd_even(nums):
    for n in nums:
        if n%2==0:
            print(f'{n} is Even')
        else:
            print(f'{n} is Odd')
#         time.sleep(1)

nums = [3,5,7,9,11,13]
nums1 = [1,2,3,4,5,6]
thread1 = threading.Thread(target=calc_sq,args=(nums,))
thread2 = threading.Thread(target=calc_cube,args=(nums,))
thread3 = threading.Thread(target=odd_even,args=(nums1,))

start = time.perf_counter()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.perf_counter()

print(f"Total time:{end-start}")
