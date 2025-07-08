# 소트인사이드 (1427)

import sys

# 내림차순 정렬 함수
def sortdown (list):
    down = sorted(list, reverse=True) # 내림차순 정렬
    result = ''.join(down)
    return(result)


N = sys.stdin.readline() # input은 느리므로 sys.stdin.readline() 사용
print(sortdown(N))