# 피보나치 수 3 (2749번)

"""

"""

import sys

def fibo (n):
    x, y = 0, 1
    for _ in range(n):
        temp = x
        x = y
        y = (temp+y) % 1000000
    return x
        

n = int(sys.stdin.readline())
n = n % 1500000  # 피사노 주기 적용

print(fibo(n))
