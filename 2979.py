import sys
from collections import Counter
A, B, C = map(int, sys.stdin.readline().strip().split())
truck = [0 for _ in range(100)]
for _ in range(3) : 
    S, E = map(int, sys.stdin.readline().strip().split())
    for i in range(S-1, E-1) :
        truck[i] += 1
c = Counter(truck)
print(c[1]*A + c[2] * B * 2 + c[3]* C * 3)
## 한 대당 요금임을 간과하지 않기!