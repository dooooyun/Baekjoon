# 돌 게임 5 (9659번)

"""
짝수 일 때 CY 홀수 일 때 SK
"""

import sys

n = int(sys.stdin.readline())

if n % 2 == 0:
    print("CY")
else:
    print("SK")