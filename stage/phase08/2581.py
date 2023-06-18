M = int(input())
N = int(input())

sosu = []
for i in range(M, N+1) : 
    if i > 1 : 
        error = 0
        for k in range(2, i) : 
            if i%k == 0 : 
                error += 1
                break
        if error == 0 : 
            sosu.append(i)
if len(sosu) > 0 : 
    print(sum(sosu))
    print(min(sosu))
else : 
    print(-1)