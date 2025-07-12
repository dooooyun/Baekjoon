from collections import deque

n = int(input())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()       # 맨 위 버리기
    q.append(q.popleft())  # 그 다음 맨 아래로

print(q[0])  # 마지막 카드 출력