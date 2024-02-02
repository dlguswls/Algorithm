import sys

N, S, P = map(int, sys.stdin.readline().split())

if N > 0 : 
    scores = list(map(int, sys.stdin.readline().split()))
    if N == P and scores[-1] >= S : 
        print(-1)
    else : 
        res = N+1
        for i in range(N) : 
            if scores[i] <= S : 
                res = i+1
                break
        print(res)
else : 
    print(1)

