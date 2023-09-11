import sys
M = int(sys.stdin.readline().strip())

S = set()
for i in range(M) : 
    command = sys.stdin.readline().strip().split()
    if len(command) == 1 : 
        if command[0] == 'all' : 
            S = set([i for i in range(1, 21)])
        else : 
            S = set()
    else : 
        c = command[0]
        n = int(command[1])
        if c == "add" : 
            S.add(n)
        elif c == 'remove' : 
            S.discard(n)
        elif c == 'check' : 
            if n in S : 
                print(1)
            else : 
                print(0)
        else :
            if n in S : 
                S.remove(n)
            else : 
                S.add(n)
