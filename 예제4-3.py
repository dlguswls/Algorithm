import sys
loc = sys.stdin.readline().strip()
steps = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (1, -2), (2,-1)]
x = int(loc[1])
y = int(ord(loc[0])) - int(ord('a')) + 1

cnt = 0
for step in steps : 
    k = x + step[0]
    q = y + step[1]
    if k <=0 or q <=0 or k > 8 or q > 8 : 
        continue
    cnt += 1
print(cnt)