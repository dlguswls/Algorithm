import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

s = str(a * b * c)

cnt = [0]*10
for i in s:
    cnt[int(i)] += 1

for i in cnt:
    print(i)