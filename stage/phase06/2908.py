import sys
a, b = sys.stdin.readline().split()
a_ = ''
b_ = ''
for i in range(len(a)-1, -1, -1) :
    a_ += a[i]
for i in range(len(b)-1, -1, -1) :
    b_ += b[i]
print(max(int(a_), int(b_)))