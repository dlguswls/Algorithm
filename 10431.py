from bisect import bisect_left
import sys

M = int(sys.stdin.readline().strip())
for i in range(M) : 
    data = list(map(int, sys.stdin.readline().strip().split()))
    number = data[0]
    t = data[1:]

    cnt = 0
    for i in range(1, 20) :
    # for i in range(1, 2) : 
        student = t[:i]
        # print(student)
        if max(student) < t[i] : 
            continue
        else : 
            idx = bisect_left(student, t[i])

            cnt += (len(student) - idx)
            t[:i+1] = student[:idx] + [t[i]] + student[idx:]            
    print(number, cnt)
