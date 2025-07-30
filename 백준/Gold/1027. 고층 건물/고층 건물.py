# 고층 건물 (1027번)

"""
왼쪽은 보이는 기울기가 그 전 건물보다만 작으면 보임
오른쪽은 보이는 기울기가 그 전 건물보다만 크면 보임
"""

import sys
input = sys.stdin.readline

# 입력
n = int(input())
buildings = list(map(int, input().split()))

max_see = 0
for i in range(n):
    count = 0

    # 왼쪽
    min_lean = float('inf')
    for j in range(i-1, -1, -1):
        lean = (buildings[i] - buildings[j]) / (i - j)
        if lean < min_lean:
            min_lean = lean
            count += 1

    # 오른쪽
    max_lean = float('-inf')
    for j in range(i + 1, n):
        lean = (buildings[i] - buildings[j]) / (i - j)
        if lean > max_lean:
            max_lean = lean
            count += 1
    
    max_see = max(max_see, count)

#최대로 건물을 볼 수 있는 건물 출력
print(max_see)