# def func1(n) :
#     sum = 0
#     for i in range(1, n+1) :
#         if i % 3 == 0 :
#             sum += i
#             continue
#         if i % 5 == 0 :
#             sum += i
#     return sum
# print(func1(16))

# def func2(arr, n) : 
#     for i in range(n-1):
#         for j in range(i+1, n) : 
#             if arr[i]+arr[j] == 100 : 
#                 return 1
#     return 0
# print(func2([4, 13, 63, 87],4))

# def func3(n) : 
#     temp = n**0.5
#     if int(temp) == temp:
#             return 1
#     return 0

# print(func3(756580036))


def func4(n) : 
    i = 0
    sum = 0
    while 2**i < n : 
          i += 1
    return 2**(i-1)
    
print(func4(97615282))

