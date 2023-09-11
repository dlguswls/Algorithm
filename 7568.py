import sys

N = int(sys.stdin.readline().strip())
students = []
for i in range(N) : 
    students.append(list(map(int, sys.stdin.readline().strip().split())))
for i in students : 
    cnt = 1
    for j in students : 
        if i[0] < j[0] and i[1] < j[1] : 
            cnt += 1
    print(cnt)