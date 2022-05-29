import time
import numpy as np

# Linear search

def find_l (massive, x):
    for i in range(len(massive)):
        if massive[i] == x:
            return i
    return -1

# Binary search

def find_b (massive, x):
    low = 0
    high = len(massive)-1
    while low<=high:
        mean = (low+high)//2
        if massive[mean] == x:
            return mean
        elif massive[mean] > x:
            high = mean
        else:
            low = mean + 1
    return -1

# Speed check

massive = np.arange(10000)
x = massive[8970]

start = time.perf_counter()
find_l(massive, x)
finish_start = time.perf_counter()
find_b(massive, x)
finish = time.perf_counter()

print(f"Linear search: {finish_start-start:0.6f} seconds")
print(f"Binary search: {finish-finish_start:0.6f} seconds")