import sys
input = sys.stdin.readline

a = [int(input()) for i in range(9)]
a.sort()
print('---')

for i in range(9):
    for j in range(i+1, 9):
        if sum(a) - (a[i] + a[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else: 
                    print(a[k])
                break

        break

