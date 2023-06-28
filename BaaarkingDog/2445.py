import sys
input = sys.stdin.readline().strip()

n = int(input)

for i in range(n):
    print('*' * (i+1), end = '')
    print(' ' * ((n-i-1)*2), end = '')
    print('*' * (i+1))

for i in range(n-1):
    print('*' * (n - 1 - i), end = '')
    print(' ' * ((i + 1)*2), end = '')
    print('*' * (n - 1 - i))