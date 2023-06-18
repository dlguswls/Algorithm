def sosu(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

sosu_nums = []
for i in range(4, 5001) :
    if sosu(i) :
        sosu_nums.append(i)

k = int(input())
for i in range(k) :
    N = int(input())
    hubo = N//2
    print(hubo)
    for j in range(hubo) :
        if hubo in sosu_nums  :
            print(N-hubo)
            if sosu(N-hubo) :
                print(hubo, N-hubo)
                break
            else :
                hubo -= 1
        else :
            hubo -= 1
            print(hubo)