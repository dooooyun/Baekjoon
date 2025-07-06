#진법 변환 (2745)

import math

def decimal_change(N, B): # 10진법으로 변환해주는 함수 작성
    # 변수 선언
    number = 0
    N = N[::-1] # 숫자를 1의 자리부터 가야 편하므로 뒤집어줌

    # N의 자릿수를 차례대로 올라가며 숫자 계산
    for i in range(len(N)):
        if '0' <= N[i] <= '9': # N의 i자릿수가 숫자이면 그냥 계산
            number += int(N[i])*(B**i)
        else: # N의 i자릿수가 알파벳이면 아스키코드를 사용하여 정수로 변환하여 계산
            number += (ord(N[i])-55)*(B**i)

    # 나온 숫자 값을 리턴해줌
    return number

# 입력, 출력
N, B = input().split()
B = int(B)
print(decimal_change(N, B))
