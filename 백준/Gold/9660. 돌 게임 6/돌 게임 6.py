# 돌 게임 6 (9660번)

"""
1 - sk
2 - 1 1 cy
3 - 3 sk
4 - 4 sk
5 - 1 4 cy, 3 1 1 sk => sk
6 - 1 1 4 sk, 3 3 cy, 4 1 1 sk => sk
7 - 4 3 cy, 3 4 cy, 1 6(sk) cy => cy
8 - 4 4 cy, 3 3 1 1 cy, 1 7(cy) sk => sk
9 - 4 5(sk) cy, 3 6(sk) cy, 1 8(sk) cy => cy
10 - 4 6(sk) cy, 3 7(cy) sk => sk
11 - 4 7(cy) sk => sk
12 - 4 8(sk) cy, 3 9(cy) sk => sk
13 - 4 9(cy) sk
14 - 4 10(sk) cy, 3 11(sk) cy, 1 13(sk) cy => cy
15 - 4 11(sk) cy, 3 12(sk) cy, 1 14(cy) sk => sk
"""

import sys

n = int(sys.stdin.readline())

if n % 7 == 0 or n % 7 == 2:
    print("CY")
else:
    print("SK")