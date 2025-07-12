import sys
input = sys.stdin.readline

k = int(input())     # 숫자 개수 입력
stack = []

for _ in range(k):
    num = int(input())
    if num == 0:
        # 0이면 직전 수 제거 (pop)
        if stack:
            stack.pop()
    else:
        # 0이 아니면 스택에 추가
        stack.append(num)

# 최종 합 출력
print(sum(stack))