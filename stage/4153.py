while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break
    else :
        max_num = max(a)
        a.remove(max_num)
        if max_num**2 == a[0]**2+a[1]**2 :
            print('right')
        else : print('wrong')