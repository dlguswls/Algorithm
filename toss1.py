from itertools import permutations
import sys

input = sys.stdin.readline
s = input().strip()
n = int(input().strip())

items = [str(x+1) for x in range(n)]
n_items = list(map(''.join, permutations(items, n)))
n_items.sort(reverse = True)

for i in n_items:
    if i in s:
        print(int(i))
        break
    else :
        answer = -1