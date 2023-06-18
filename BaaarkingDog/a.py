def func1(n) :
    sum = 0
    for i in range(1, n+1) :
        if i % 3 == 0 :
            sum`+= i
            continue
        if i % 5 == 0 :
            sum += i
    return sum
print(func1(16))
