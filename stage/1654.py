K, N = map(int, input().split())
lens = [int(input()) for _ in range(K)]
min_len = min(lens)
count = 0
for i in range(min_len, 1, -1) :
    if count>=N :
        print(i+1)
        break
    count = 0
    for k in lens :
        count += (k//i)