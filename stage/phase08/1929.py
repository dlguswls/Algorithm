# 시간초과
# M, N = map(int, input().split())
# for i in range(M, N+1) : 
#     no_sosu = 0
#     if i >= 2 : 
#         for k in range(2, i) : 
#             if i%k == 0 : 
#                 no_sosu += 1
#                 break
#     else : 
#         no_sosu += 1
#     if no_sosu == 0 : 
#         print(i)

# 시간 초과
# M, N = map(int, input().split())
# for i in range(M, N+1) : 
#     if i == 1 : 
#         pass
#     elif i==2 : 
#         print(i)
#     else : 
#         sosu = 0
#         for k in range(2, int(i*0.5)+1) : 
#             if i%k == 0 : 
#                 sosu += 1 
#                 break
#         if sosu == 0 : 
#             print(i)

# 시간 초과
# M, N = map(int, input().split())
# def findPrimary(n) : 
#     if n == 1 : 
#         return False
#     else : 
#         for k in range(2, int(n*0.5)+1) : 
#             if n % k == 0 : 
#                 return False
#         return True

# for i in range(M, N+1) : 
#     if findPrimary(i) : 
#         print(i)

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: #1은 소수가 아뉘지!
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)