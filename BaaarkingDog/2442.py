import sys
input = sys.stdin.readline().strip()

n = int(input)

for i in range(n):
    empty = n - i - 1
    print(' ' * empty, end = '')
    print('*' * (2 * (i+1) -1))