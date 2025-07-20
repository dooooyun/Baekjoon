# 좌표 정렬하기 (11650번)

"""
"""

import sys

n = int(sys.stdin.readline())

points = [tuple(map(int, input().split())) for _ in range(n)] 

# x 오름차순, x 같으면 y 오름차순
points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(x, y)