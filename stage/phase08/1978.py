N = int(input())
nums = list(map(int, input().split()))

for i in nums : 
    if i < 2 : 
        N -= 1
        pass
    for k in range(2, i) : 
        if i%k == 0 : 
            N -= 1
            break
print(N)