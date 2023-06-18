import sys
a = []
for i in range(10) : 
    n = int(sys.stdin.readline())
    a.append(n%42)
arr = set(a)
print(len(arr))

