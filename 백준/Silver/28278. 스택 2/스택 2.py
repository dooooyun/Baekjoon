import sys

input = sys.stdin.readline

# 스택 리스트 선언
stack = []

# 명령 개수
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        # 1 X : push
        stack.append(int(command[1]))
    
    elif command[0] == '2':
        # 2 : pop
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == '3':
        # 3 : length
        print(len(stack))

    elif command[0] == '4':
        # 4 : empty
        print(1 if not stack else 0)

    elif command[0] == '5':
        # 5 : top
        if stack:
            print(stack[-1])
        else:
            print(-1)