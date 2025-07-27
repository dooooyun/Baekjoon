import sys
input = sys.stdin.readline

n = int(input())
friends = [set() for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friends[a].add(b)
    friends[b].add(a)

stack = [(1, [], [])]  # (현재 학생 번호, team1, team2)

while stack:
    idx, team1, team2 = stack.pop()

    if idx > n:
        # 완전 그래프 검사
        ok1 = all((j in friends[i]) for i in team1 for j in team1 if i != j)
        ok2 = all((j in friends[i]) for i in team2 for j in team2 if i != j)

        if ok1 and ok2:
            print(1)
            # 🔥 1번 학생이 포함된 팀을 먼저 출력!
            if 1 in team1:
                print(*sorted(team1), -1)
                print(*sorted(team2), -1)
            else:
                print(*sorted(team2), -1)
                print(*sorted(team1), -1)
            sys.exit()
        continue

    # team1 시도
    if all(idx in friends[member] for member in team1):
        stack.append((idx + 1, team1 + [idx], team2))

    # team2 시도
    if all(idx in friends[member] for member in team2):
        stack.append((idx + 1, team1, team2 + [idx]))

# 불가능한 경우
print(-1)