import sys
A, B, C = map(int, sys.stdin.readline().strip().split())
truck = [0 for _ in range(100)]
for _ in range(3) : 
    start, end = map(int, sys.stdin.readline().strip().split())
    for i in range(start-1, end-1) : 
        truck[i] += 1
from collections import Counter
truck_count = Counter(truck)
print(A * truck_count[1] + B * truck_count[2] * 2 + C * truck_count[3] * 3)