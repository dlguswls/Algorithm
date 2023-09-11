import sys
M, k = map(int, sys.stdin.readline().strip().split())
medals = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)

idx = [medals[i][0] for i in range(M)].index(k)

for i in range(M) : 
    if medals[idx][1:] == medals[i][1:] : 
        print(i+1)
        break