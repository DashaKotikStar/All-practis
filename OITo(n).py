import time
import math

def func1(arr):
    s = 0
    for x in arr:
        s = s + x
    return s


def func2(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            count = count + 1
    return count


def func3(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def zamery(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


n_list = [10000, 20000, 40000, 80000]

print("n\tвремя1(O(n))\tвремя2(O(n²))\tвремя3(O(log n))")

for n in n_list:
    arr = list(range(n))

    t1 = zamery(func1, arr)

    t2 = zamery(func2, arr)

    t3 = zamery(func3, arr, n - 1)

    print(f"{n}\t{t1:.6f}\t{t2:.6f}\t{t3:.6f}")