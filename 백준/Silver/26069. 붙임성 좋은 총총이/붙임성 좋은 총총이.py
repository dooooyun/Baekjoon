# 붙임성 좋은 총총이 (26069번)

# 변수들
count = 0
n = int(input())
visited = set() # set 함수로 중복을 없앰
visited.add("ChongChong") # 총총이는 춤을 추고 있으니 넣어놓고 시작

for _ in range(n):
    a, b = input().split()
    if a in visited or b in visited: # 붙은 문자열 두개 중 하나라도 visited에 있으면 두 문자열 다 추가
        visited.add(a)
        visited.add(b)

count += len(visited)

print(count)