import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
n = int(input()) 

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        # 1 X: 정수 X를 덱 앞에 넣기
        dq.appendleft(int(command[1]))

    elif command[0] == '2':
        # 2 X: 정수 X를 덱 뒤에 넣기
        dq.append(int(command[1]))

    elif command[0] == '3':
        # 3: 덱 앞에서 꺼내기
        print(dq.popleft() if dq else -1)

    elif command[0] == '4':
        # 4: 덱 뒤에서 꺼내기
        print(dq.pop() if dq else -1)

    elif command[0] == '5':
        # 5: 덱에 들어있는 정수 개수
        print(len(dq))

    elif command[0] == '6':
        # 6: 덱이 비어있으면 1, 아니면 0
        print(1 if not dq else 0)

    elif command[0] == '7':
        # 7: 덱 앞에 있는 정수 출력
        print(dq[0] if dq else -1)

    elif command[0] == '8':
        # 8: 덱 뒤에 있는 정수 출력
        print(dq[-1] if dq else -1)