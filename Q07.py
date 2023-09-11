import sys
n = sys.stdin.readline().strip()
n1 = 0
n2 = 0
for i in range(len(n)) : 
    if i < len(n)//2 : 
        n1 += int(n[i])
    else : 
        n2 += int(n[i])
if n1 == n2 : 
    print("LUCKY")
else : 
    print("READY")