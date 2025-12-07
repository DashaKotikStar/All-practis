import time
import math

def func1(n):
    s = 0
    for i in range(n):
        s += i
    return s
def func2(n):
    s = 0
    for i in range(len(n)):
        for j in range(len(n)):
            s += 1
    return s
def func3(n):
    fact = math.factorial(n)
    s = 0
    for i in range(len(n)):
        s += 1
    return s
def zamery(func, n):
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start

print("\t \t время1\t \t время2")
for a in [100000, 200000, 300000, 400000, 500000]:
    t1 = zamery(func1, a)
    t2 = zamery(func2, a)
    print(f"{a}\t{t1:.6f}\t{t2:.6f}")

print("\n\tвремя3")
for b in [100, 200, 300, 400, 500, 600, 700, 800]:
    t3 = zamery(func3, b)
    print(f"{b}\t{t3:.6f}")