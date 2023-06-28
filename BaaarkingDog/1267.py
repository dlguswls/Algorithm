# 핸드폰 요금
## 영식 요금제 : 30초마다 10원씩 청구
## 민식 요금제 : 60초마다 15원씩 청구

import sys
input = sys.stdin.readline

n = input()
times = list(map(int, input().split()))

y = 0
for time in times :
    y += (time//30 + 1) * 10
m = 0
for time in times :
    m += (time//60 + 1) * 15

if y < m : 
    print("Y", y)
elif m < y :
    print("M", m)
else:
    print("Y", "M", y)