def shape(n):
    # n = 1이면 *하나 출력
    if n == 1:
        return ['*']
    
    # n/3 크기의 별을 재귀적으로 생성
    stars = shape(n // 3)
    result = []

    for i in range(n): # n개의 줄을 생성
        if i // (n // 3) == 1:  # 가운데 줄 (n = 9라면 3~5줄이 가운데 부분)
            result.append(
                stars[i % (n // 3)] + ' ' * (n // 3) + stars[i % (n // 3)] # 별 하나를 반복되는 패턴의 사각형이라고 생각
            )
        else:
            result.append( # 위, 아랫 줄
                stars[i % (n // 3)] * 3
            )
    return result

# 입력, 출력
n = int(input())
output = shape(n)
print('\n'.join(output))