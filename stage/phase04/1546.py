import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
big = max(a)
new_a = []
for i in a : 
    new_a.append(i/big*100)
print(sum(new_a)/n)