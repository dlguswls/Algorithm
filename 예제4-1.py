import sys
n = int(sys.stdin.readline().strip())
f = [1, 1]
move = list(sys.stdin.readline().strip().split())
for i in move:
    if i == "U":
        if f[0] - 1 > 0 : 
            f[0] -= 1
        else : 
            continue
    elif i == "R" : 
        if f[1] + 1 <= n : 
            f[1] += 1
        else : 
            continue
    elif i == "L" : 
        if f[1] - 1 > 0 : 
            f[1] -= 1
        else : 
            continue
    else : 
        if f[0] <= n : 
            f[0] += 1
        else : 
            continue
for k in f : 
    print(k, end = ' ')