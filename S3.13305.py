# N개의 도시는 수평 방향으로 일직선상에 존재
# 제일 왼쪽에서 오른쪽으로 이동하고자 함
# 인접한 두 도시 사이의 도로들은 서로 길이 다를 수 있음 ( km 단위 )
# 도로 1km 이동하는 데에 1리터의 기름 사용
# 주유소는 도시마다 하나이며, 리터당 가격 다름
# 최소 비용으로 이동 가능한 방법 찾기

import sys

N = int(sys.stdin.readline().strip()) # 도시 개수
lines = list(map(int, sys.stdin.readline().split())) # 도로 길이
stations = list(map(int, sys.stdin.readline().split())) # 주유소 가격

pay = lines[0] * stations[0]
mini = stations[0]
for i in range(1, N-1) : 
    if stations[i] < mini : 
        pay += lines[i] * stations[i]
        mini = stations[i]
    else : 
        pay += lines[i] * mini
    
print(pay)