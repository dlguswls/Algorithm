n = int(input())

a = 0  # 분자
b = 0  # 분모

cnt = 0
while n>0 : 
    cnt += 1
    n -= cnt
k = n+cnt

if cnt%2 ==0 : 
    a = k
    b = cnt-k+1
else : 
    b = k
    a = cnt-k+1

print(str(a)+'/'+str(b))
