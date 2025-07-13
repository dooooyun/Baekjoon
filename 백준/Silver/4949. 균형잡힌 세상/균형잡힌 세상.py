from collections import deque

while True:
    is_vps = True
    sentence = input()
    if sentence == '.': # .이 나오면 문장 끝
        break

    ps = deque()
    
    for ch in sentence:
        if ch == '(' or ch == '[': # ch가 '(' or '[' 이면 일단 ps가 넣음
            ps.append(ch)
        elif ch == ')': # ch가 ')'이면 가장 최근에 들어있던 괄호가 짝인지 확인 
            if not ps or ps[-1] != '(': # 짝이 아니면 false
                is_vps = False
                break
            elif ps[-1] == '(': # 짝이 맞으면 두 짝을 빼고 다시 시작
                ps.pop()
        elif ch == ']':
            if not ps or ps[-1] != '[':
                is_vps = False
                break
            elif ps[-1] == '[':
                ps.pop()
    
    if ps: # ps가 비어있지 않으면 false
        is_vps = False

    print("yes" if is_vps else "no")