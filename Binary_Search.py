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