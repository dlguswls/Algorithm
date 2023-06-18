n = int(input())
a_list = []
b_list = []
for i in range(n) : 
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
for i in range(n) : 
    a1 = a_list[i]
    b1 = b_list[i]
    sum = a1 + b1
    print('Case #'+str(i+1)+': '+str(a1)+' + '+str(b1)+' = '+str(sum))