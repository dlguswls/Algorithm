import sys
A, B, V = map(int, sys.stdin.readline().split())

# k : 올라가는 데 걸리는 일수
# A*k-B*(k-1) >= V
# (A-B)k+B >= V
# k >= (V-B)/(A-B)

k = (V-B)/(A-B)
print(int(k) if k == int(k) else int(k)+1)