import sys
n = int(sys.stdin.readline())
for i in range(n) : 
    q = sys.stdin.readline()
    total_score = 0
    cnt = 0
    for k in q : 
        if k == 'O' : 
            cnt +=1 
            total_score += cnt
        else : 
            cnt = 0
    print(total_score)