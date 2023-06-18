nums = []
while True :
    a = int(input())
    if a == 0 :
        break
    nums.append(a)

def palindrome(num) :
    for i in range(int(len(str(num))*0.5)) :
        if str(num)[i] != str(num)[-1-i] :
            return 'no'
    return 'yes'
for i in nums :
    print(palindrome(i))