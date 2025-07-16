# 인사성 밝은 곰곰이 (25192번)

# 변수들
count = 0
n = int(input())
visited = set()

for _ in range(n):
    chat = input()
    if chat == "ENTER": # 채팅이 ENTER이면 visited를 초기화해줌
        count += len(visited)
        visited.clear()
    else: # 채팅을 추가해줌 (set을 사용하여 중복제거)
        visited.add(chat)

count += len(visited)

print(count)