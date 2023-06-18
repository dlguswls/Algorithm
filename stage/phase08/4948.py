<<<<<<< HEAD
# 코드 안끝남..
=======
# 코드가 안끝남..
>>>>>>> fc9c8c66736db2dd43fd2b2be1242992fd77e21e
# arr_all = []
# while True:
#     arr = []
#     num = int(input())
#     if num == 0:
#         break
#     for n in range(num+1, 2*num+1):
#         if n == 1:
#             continue
#         for i in range(2, int(n*0.5)+1):
#             if n % i == 0:
#                 break
#         else:
#             arr.append(n)
#     arr_all.append(len(arr))
#
# for i in arr_all:
#     print(i)

# 정답 코드
def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음

# 이건 뭔소린지 모르겠음
# import sys
# input = sys.stdin.readline
# inputList = list()
# N = 123456*2 + 1   # 246913
# isPrime = [True] * N
# print(isPrime)
# for i in range(2, int(N**0.5)+1):
#     if isPrime[i]:
#         for j in range(2*i, N, i):
#             isPrime[j] = False
#
# def counting(inputValue):
#     cnt = 0
#     for k in range(inputValue+1, inputValue*2 + 1):
#         if isPrime[k]:
#             cnt += 1
#     print(cnt)
#
#
# while True:
#     k = int(input())
#     if not k:
#         break
#     counting(k)
