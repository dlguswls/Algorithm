# 검색...
import sys
n = int(sys.stdin.readline())
count = 1
stack_range = []
plus_minus = []
message = True

for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack_range.append(count)
        plus_minus.append('+')
        count += 1
    if stack_range[-1] == num:
        stack_range.pop()
        plus_minus.append('-')
    else:
        message = False
        print('NO')
        break

if message == True:
    for i in plus_minus:
        print(i)


