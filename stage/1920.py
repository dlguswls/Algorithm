import sys
N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split())) ###
M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())
for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)

## 포함 여부 파악하는 시간 복잡도
# 리스트의 in연산자를 통한 포함 여부의 시간 복잡도는 O(N)
# 이분 탐색의 시간 복잡도는 O(logN)
# Set과 Dictionary의 in연산을 통한 포함 여부 확인의 시간 복잡도는 O(1)
## N_list가 list면 시간초과 되고 set이면 통과!