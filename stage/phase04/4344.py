import sys
n = int(sys.stdin.readline())
for _ in range(n) : 
    a = list(map(int, sys.stdin.readline().split()))
    num_student, scores = a[0], a[1:]
    mean_score = sum(scores)/num_student
    cnt = 0
    for i in scores : 
        if i>mean_score : 
            cnt +=1
    result = cnt/num_student*100
    print('%.3f'%result+'%')