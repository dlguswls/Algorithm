import sys
a = []
for i in range(9) : 
    a1 = int(sys.stdin.readline())
    a.append(a1)
big = max(a)
print(big)
print(a.index(big)+1)