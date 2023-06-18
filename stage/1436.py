end_N = []
count = 0
num = 666
while True :
    if count>10000 :
        break
    if '666' in str(num) :
        end_N.append(num)
        count+=1
    num +=1
a = int(input())
print(end_N[a-1])