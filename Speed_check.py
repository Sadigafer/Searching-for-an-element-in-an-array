import time
import numpy as np
from Linear_Search import find_l as LS
from Binary_Search import find_b as BS

# Speed check

massive = np.arange(10000)
x = massive[8970]

start = time.perf_counter()
LS(massive, x)
finish_start = time.perf_counter()
BS(massive, x)
finish = time.perf_counter()

print(f"Linear search: {finish_start-start:0.6f} seconds")
print(f"Binary search: {finish-finish_start:0.6f} seconds")