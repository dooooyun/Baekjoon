# Fly me to the Alpha Centauri (1011번)

"""
이동 패턴: 1 → 2 → 3 → ... → n → ... → 2 → 1
n는 d 이하의 최대 정수 제곱근이라 할 때
이동 횟수
n의 제곱이 정확히 d일 때는 위의 상황이므로 2n - 1
d가 n제곱보다 큰데 n을 한 번 더 간거 보단 작거나 같다면 1~n사이의 수를 한 번만 더 가면 됨 -> 2n
d가 n제곱 + n 한거보다 크다면 n을 가고 또 n+1만큼 가줘야함 -> 2n + 1
"""

import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    n = int(math.sqrt(d))

    if d == n**2:
        print(2*n - 1)
    elif d <= n**2 + n:
        print(2*n)
    else:
        print(2*n + 1)