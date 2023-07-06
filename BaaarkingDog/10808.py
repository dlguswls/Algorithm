import sys
input = sys.stdin.readline().strip()

arr = input

cnt = [0]*26

for i in arr:
    # 아스키 코드 활용
    # a의 아스키 코드는 97
    cnt[ord(i)-97]+=1

print(*cnt)
