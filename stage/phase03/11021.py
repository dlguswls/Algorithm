n = int(input())
a_list = []
b_list = []
for i in range(n) : 
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
for i in range(n) : 
    print('Case #'+str(i+1)+': '+str(a_list[i] + b_list[i]))