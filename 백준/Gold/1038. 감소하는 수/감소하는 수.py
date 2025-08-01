# 감소하는 수 (1038번)

"""
1, 2, 3, 4, 5, 6, 7, 8, 9
=> 9개

10
20, 21
30, 31, 32
40, 41, 42, 43
...
90, 91, 92, 93, 94, 95, 96, 97, 98
=> 45개

210 -> 1
310 | 320, 321 -> 1 + 2
410 | 420, 421 | 430, 431, 432 -> 1 + 2 + 3
500 -> 1+2+3+4 (4*5/2)
600 -> 1+2+3+4+5
700 -> 1+2+3+4+5+
800 -> 1+2+3+4+5+6+7
900 -> 1+2+3+4+5+6+7+8
...

3210 -> 1
4210 | 4310, 4320, 4321 1 -> 1+3
5210 | 5310, 5320, 5321 | 5410, 5420, 5421, 5430, 5431, 5432 -> 1+3+6
6210 | 6310, 6320, 6321 | 6410, 6420, 6421, 6430, 6431, 6432 | 6510, 6520, 6521, 6530, 6531, 6532, 6540, 6541, 6542, 6543 -> 1+3+6+10
7000 -> 1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)
8000 -> 1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)
9000 -> 1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)+(1+2+3+4+5+6+7)

54321 -> 1

아닌듯..

감소하는 수 라는건 애초에 중복되지 않는 수를 뽑기만 하면 순서를 신경쓰지 않아도 됨 -> 조합 (5, 6을 뽑으면 무조건 65밖에 안되기때문)
"""

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for digit in range(1, 11): # 0~9 수를 중복없이 넣으려면 최대 10자리임
    for comb in combinations(range(10), digit): # 정수 리스트 형식으로 digit갯수를 뽑음
        num = int(''.join(map(str, sorted(comb, reverse=True)))) # 뽑은 정수를 내림차순으로 정렬하여 하나로 만듦
        nums.append(num)

decreasing_nums = sorted(nums) # 넣은 수들을 오름차순으로 정렬

if n < len(decreasing_nums):
    print(decreasing_nums[n])
else:
    print(-1)