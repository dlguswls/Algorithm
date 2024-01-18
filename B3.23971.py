## 내 풀이
import sys
H, W, N, M = map(int, sys.stdin.readline().split())
if W % (M+1) > 0: 
    x = W//(M+1) + 1
else : x = W//(M+1)
if H % (N+1) > 0: 
    y = H//(N+1) + 1
else : y = H//(N+1)
print(x*y)

## 검색
H,W,N,M = list(map(int,input().split(' ')))
#math.ceil()함수는 숫자의 올림을 계산해 줍니다
import math
a = math.ceil(H/(N+1)) # 세로에 몇 명이 앉는지를 계산합니다
b = math.ceil(W/(M+1)) # 가로에 몇 명이 앉는지를 계산합니다
answer = a*b #가로와 세로의 값을 곱합니다
print(answer)