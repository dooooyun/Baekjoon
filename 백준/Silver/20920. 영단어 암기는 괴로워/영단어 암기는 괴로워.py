# 통계학 (2108번)

import sys
input = sys.stdin.readline

from collections import Counter

# 변수들
n, m = map(int, input().split())
words = []

for _ in range(n):
    word = input().strip()  # input.strip을 받으면 \n이나 공백을 제거해줘 단어 비교에 좋음
    if(len(word) >= m): # m보다 긴 단어들만 사용
        words.append(word)

counts = Counter(words) # 빈도수를 나타내줌

# 1순위로 빈도수를 내림차순으로, 2순위로 길이를 내림차순으로, 3순위로 알파벳순을 오름차순으로 정렬
sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], -len(w), w))

for w in sorted_words:
    print(w)