## 비밀번호 발음하기 ##
# 1. 모음(a, e, i, o, u) 반드시 포함
# 2. 모음 3개 or 자음 3개 연속 배치 X
# 3. 같은 글자 연속 두 번 X ( ee, oo 허용 )
# 대문자 X, 1~20 글자 사이, 마지막은 end

import sys

while True : 
    p = sys.stdin.readline().strip()
    if p == 'end' : 
        break
    vo = ['a','e','i','o','u']
    ck = [0, 1, 1]
    v = 0 # 모음 개수
    c = 0 # 자음 개수

    # 1. 모음(a, e, i, o, u) 반드시 포함
    for i in vo : 
        if i in p :
            ck[0] = 1
            break
    # 2. 모음 3개 or 자음 3개 연속 배치 X
    for i in range(len(p)) : 
        if p[i] in vo : 
            v += 1
            c = 0
            if v == 3 : 
                ck[1] = 0
                break
        else : 
            v = 0
            c += 1
            if c == 3 : 
                ck[1] = 0
                break
    # 3. 같은 글자 연속 두 번 X ( ee, oo 허용 )
    for i in range(1, len(p)) : 
        if p[i] == p[i-1] : 
            if p[i] != 'e' and p[i] != 'o' : 
                ck[2] = 0
                break
            
    if sum(ck) < 3 : 
        print('<'+p+'> is not acceptable.')
    else : 
        print('<'+p+'> is acceptable.')