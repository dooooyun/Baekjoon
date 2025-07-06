#소수 구하기

def is_prime(min, max): # 소수를 구하는 함수 작성
    # 소수인지를 판별하기 위한 배열
    prime = [True] * (max + 1)
     # 0, 1은 제외
    prime[0] = False 
    prime[1] = False

    for i in range(2, int(max**0.5)+1): # 배수를 구하는 것이므로 3*6 과 6*3은 같은 수 이기에 제곱근까지만
        if prime[i] == True: # 이미 false인 것은 건너뜀
            for j in range(i*i, max+1, i): # i*i부터 i만큼 증가하며 확인 -> i*(i-1)은 i-1순서에서 지워졌을 것이기 때문
                prime[j] = False
    # 소수인 리턴할 값들을 따로 넣어줌
    k = 0
    thisis = []
    for i in range(min, max+1):
        if prime[i] == True:
            thisis.append(i)
            k += 1

    # 소수인 수만 담은 배열을 리턴
    return thisis

#입력, 출력
M, N = map(int, input().split())
result = is_prime(M, N)
for i in result:
    print(i)