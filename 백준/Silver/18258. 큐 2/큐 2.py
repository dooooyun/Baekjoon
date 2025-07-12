import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 명령 개수 입력 받기
queue = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        # 'push X' → X를 큐의 맨 뒤에 추가
        queue.append(int(command[1]))
    
    elif command[0] == 'pop':
        # 큐에서 가장 앞 원소 제거하고 출력
        # 비어 있으면 -1 출력
        print(queue.popleft() if queue else -1)

    elif command[0] == 'size':
        # 큐에 들어있는 원소 개수 출력
        print(len(queue))

    elif command[0] == 'empty':
        # 큐가 비어 있으면 1, 아니면 0 출력
        print(0 if queue else 1)

    elif command[0] == 'front':
        # 큐의 맨 앞 원소 출력 (비어있으면 -1)
        print(queue[0] if queue else -1)

    elif command[0] == 'back':
        # 큐의 맨 뒤 원소 출력 (비어있으면 -1)
        print(queue[-1] if queue else -1)