import sys

# 입력
N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    matrix.append([int(age), name])

# 나이를 기준으로만 정렬
matrix.sort(key=lambda x: x[0])

for i in matrix:
    print(i[0], i[1])