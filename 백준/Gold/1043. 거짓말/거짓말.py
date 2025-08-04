import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

n, m = map(int, input().split())
knows = list(map(int, input().split()))
know_truth = knows[1:]

parent = [i for i in range(n + 1)]
parties = []

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)

# 진실을 아는 사람들의 대표 노드 저장
truth_roots = set(find(x) for x in know_truth)

# 각 파티가 모두 진실을 모를 경우에만 거짓말 가능
result = 0
for party in parties:
    if all(find(p) not in truth_roots for p in party):
        result += 1

print(result)