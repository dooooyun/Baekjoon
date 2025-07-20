# 단어 정렬 (1181번)

"""
"""

import sys

n = int(sys.stdin.readline())

words = []  # 일단 리스트로 입력 받기

for _ in range(n):
    word = input().strip()
    words.append(word)

# set으로 중복 제거
set_words = set(words)

# 정렬: 길이 → 사전순
sorted_words = sorted(set_words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)