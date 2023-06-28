import sys
input = sys.stdin.readline().strip()

n = int(input)

for i in range(n):
    print(' ' * i, end = '')
    print('*' * (2 * (n-i) - 1))

for i in range(n-1):
    print(' ' * (n - 1 - i - 1), end = '')
    print('*' * (2 * (i + 1) + 1))