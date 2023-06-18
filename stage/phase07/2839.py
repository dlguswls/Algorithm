# 문제점 - 이중조건문, N이5의배수이어도 바로 출력되는 게 아님!
N = int(input())
cnt = 0
cnt += N//5
if N%5 % 3 == 0 : 
    cnt += N%5//3
    print(cnt)
else :
    a = 0
    for i in range(cnt) : 
        cnt -= 1
        if (N-5*cnt) % 3 == 0 : 
            cnt += (N-5*cnt) // 3
            print(cnt)
            a = 1
            break
    if a == 0 : 
        print(-1)


## 참고
# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)