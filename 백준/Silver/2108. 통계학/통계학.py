# 통계학 (2108번)

import sys
from collections import Counter

# 변수들
n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

# 산술평균
nums_san = round(sum(nums)/n)

# 중앙값
nums.sort()
nums_mid = nums[n//2]

# 최빈값
# Counter(nums)는 각 숫자가 몇 번 나왔는지를 딕셔너리처럼 세어줍니다. 
# 예: nums = [1, 2, 2, 3, 3] → Counter({2: 2, 3: 2, 1: 1})

counter = Counter(nums)
frequency = max(counter.values()) # 횟수 중 가장 큰 값
modes = [k for k, v in counter.items() if v == frequency] # counter.item[(k, k) {수, 횟수}]중에 횟수가 2인 것
modes.sort()
if len(modes) >= 2:
    max_frequency = modes[1]
else:
    max_frequency = modes[0]

#범위
nums_range = nums[n-1] - nums[0]

print(nums_san)
print(nums_mid)
print(max_frequency)
print(nums_range)