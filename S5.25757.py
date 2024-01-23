import sys

N, G = sys.stdin.readline().strip().split()
name = []

for i in range(int(N)) : 
    n = sys.stdin.readline().strip()
    name.append(n)

name = set(name)

if G == 'Y' : 
    ans = len(name) // 1
elif G == 'F' : 
    ans = len(name) // 2
else : 
    ans = len(name) // 3
    
print(ans)