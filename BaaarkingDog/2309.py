import sys
input = sys.stdin.readline

a = [int(input()) for i in range(9)]
a.sort()

hab = sum(a)

for i in range(9):
    for j in range(i+1, 9):
        if hab - a[i] - a[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else: 
                    print(a[k])
            exit()
