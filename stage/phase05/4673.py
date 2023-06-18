raw_num = [num for num in range(10001)]
no_self_num = []
for n in raw_num : 
    self_n = n
    for i in str(n) : 
        self_n += int(i)
    no_self_num.append(self_n)
no_self_num = set(no_self_num)
for i in sorted(set(raw_num) - no_self_num) : 
    print(i)
