# 좌표 정렬하기 2 (11651)

import sys

# 좌표 오름차순 정렬 함수
def sortup (matrix):
    matrix.sort(key=lambda x: (x[1], x[0])) # y좌표를 기준으로 오름차순 정렬 y좌표 값이 같으면 x좌표 기준으로 오름차순 정렬

    return(matrix)

# 2차원 배열 입력받기
rows= int(sys.stdin.readline()) # input은 느리므로 sys.stdin.readline() 사용
cols = 2
matrix = []
for i in range(rows): # rows 갯수 만큼 받음
    row = list(map(int, sys.stdin.readline().split())) # 두 수를 list로 받음
    matrix.append(row)

result = sortup(matrix)

for i in result: # 두 수를 각각 출력
    print(i[0], i[1])