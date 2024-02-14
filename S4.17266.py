## 어두운 굴다리 ##
import sys
import math

N = int(sys.stdin.readline().strip()) # 굴다리의 길이
M = int(sys.stdin.readline().strip()) # 가로등 개수
x = list(map(int, sys.stdin.readline().strip().split())) # 가로등 위치 리스트
# 가로등의 높이가 H일 때, 왼쪾으로 H, 오른쪽응로 H 비춤

if M == 1 : 
    print(max(x[0], N-x[0]))
else : 
# 가로등 사이 거리 구하기
    distance = []
    for i in range(1, M) : 
        distance.append(x[i] - x[i-1])
    distance_max = math.ceil(max(distance)/2)

    print(max(x[0],N-x[-1], distance_max))
    # 가장 왼쪽 가로등 : x[0]
    # 가장 오른쪾 가로등 : x[-1]