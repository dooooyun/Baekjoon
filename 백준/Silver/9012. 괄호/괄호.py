t = int(input())

for _ in range(t):
    is_vps = True
    mode = 0
    ps = input()
    for ch in ps:
        if ch == '(':
            mode += 1
        else:
            mode -= 1
            if mode < 0: # 처음부터 ')' 나오는 것 방지
                is_vps = False
                break
    
    if mode != 0: # mode 값에 따라 판별
        is_vps = False
    
    print("YES" if is_vps else "NO")