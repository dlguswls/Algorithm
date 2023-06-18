import sys
a = []
for i in range(3) : 
    a.append(int(sys.stdin.readline()))
value = list(str(a[0]*a[1]*a[2]))
for i in range(10) : 
   print(value.count(str(i)))