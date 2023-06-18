n = int(input())
result = []
for i in range(n) : 
    H, M, N = map(int, input().split())

    x = N//H+1
    y = N%H
    if N%H==0 : 
        x = N//H
        y = H
    

    print(str(y)+'{:02d}'.format(x))

