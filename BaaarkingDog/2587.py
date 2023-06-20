import sys
input = sys.stdin.readline

a = []
for i in range(5) : 
    a.append(int(input()))
print(int(sum(a)/5))
print(sorted(a)[2])
