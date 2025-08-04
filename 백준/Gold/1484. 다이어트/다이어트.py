# 다이어트 (1484번)

"""
G = 현몸^2 - 기몸^2
G = (현몸+기몸)(현몸-기몸)
15 = 1*15 = 3*5
18 = 1*18 = 2*9 = 3*6
18 = [1, 2, 3, 6, 9, 18]
"""

import math
import sys
input = sys.stdin.readline

G = int(input())
now_weight = []

# 약수 짝 찾기
div = set()
for i in range(1, int(math.sqrt(G)) + 1):
    if G%i == 0:
        div.add(i)
        div.add(G//i)
sort_div = sorted(div)

# 약수 짝의 합을 2로 나눈 것이 자연수가 나온다면 짝을 지을 수 있음 (n + k)(n - k) 는 n에서 k씩 만큼 떨어진 것이기 때문
for i in range(int(len(sort_div)/2)):
    if (sort_div[i]+sort_div[len(sort_div)-i-1])%2 == 0:
        now_weight.append(int((sort_div[i]+sort_div[len(sort_div)-i-1])/2))

result = sorted(now_weight)

if not result:
    print(-1)
else:
    for w in result:
        print(w)