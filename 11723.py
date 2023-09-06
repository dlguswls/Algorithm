import sys
M = int(sys.stdin.readline().strip())
S = []
for _ in range(M) : 
    cal = sys.stdin.readline().strip().split()
    if len(cal) == 1 : 
        if cal[0] == 'all' : 
            S = [i for i in range(1, 21)]
        else : 
            S = []
    else : 
        n = int(cal[1])
        c = cal[0]
        if c == 'append' : 
            S.append(n)
        elif c == 'remove' : 
            S.remove(n)
        elif c == 'check' : 
            if n in S : 
                print(1)
            else : 
                print(0)
        else : 
            if n in S : 
                S.remove(n)
            else : 
                S.append(n)
