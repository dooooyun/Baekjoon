def shape(n):
    if n == 3:
        return ['  *  ',
                ' * * ',
                '*****']
    
    stars = shape(n // 2)
    result = []

    # 위쪽 삼각형
    for i in stars:
        result.append(' ' * (n // 2) + i + ' ' * (n // 2)) 

    # 아래쪽 두 삼각형
    for i in stars:
        result.append(i + ' ' + i)
    
    return result

# 입력, 출력
n = int(input())
result = shape(n)
print('\n'.join(result))