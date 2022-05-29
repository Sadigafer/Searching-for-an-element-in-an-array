# Linear search

def find_l (massive, x):
    for i in range(len(massive)):
        if massive[i] == x:
            return i
    return -1

