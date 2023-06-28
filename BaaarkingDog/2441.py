import sys
input = sys.stdin.readline().strip()

n = int(input)

for i in range(n):
    print(' '*i, end = '')
    print('*'*(n-i))
   