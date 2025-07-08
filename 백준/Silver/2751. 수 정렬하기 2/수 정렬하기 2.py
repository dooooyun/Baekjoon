# 수 정렬하기 2 (2751)

import sys

# 오름차순 정렬 함수
def sortup (list):
    up = sorted(list) # 오름차순 정렬
    return(up)


N = int(sys.stdin.readline()) # input은 느리므로 sys.stdin.readline() 사용
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline())) # 정수 하나씩 받음

result = sortup(arr)
for i in result:
    print(i)