n = int(input())

for k in range(n) :
    floor = int(input())  # 층수
    num = int(input())  # 호수
    a = [x for x in range(1, num+1)]
    for i in range(floor) : 
        for j in range(1, num) : 
            a[j] += a[j-1]
    print(a[-1])
