# import sys
# n = int(sys.stdin.readline().strip())
# f = [1, 1]
# move = list(sys.stdin.readline().strip().split())
# for i in move:
#     if i == "U":
#         if f[0] - 1 > 0 : 
#             f[0] -= 1
#         else : 
#             continue
#     elif i == "R" : 
#         if f[1] + 1 <= n : 
#             f[1] += 1
#         else : 
#             continue
#     elif i == "L" : 
#         if f[1] - 1 > 0 : 
#             f[1] -= 1
#         else : 
#             continue
#     else : 
#         if f[0] <= n : 
#             f[0] += 1
#         else : 
#             continue
# for k in f : 
#     print(k, end = ' ')

import sys
n = int(sys.stdin.readline().strip())
x, y = 1, 1
plans = sys.stdin.readline().strip().split()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
move_type = ['R', 'D', 'L', 'U']

for plan in plans : 
    for i in range(len(move_type)) : 
        if move_type[i] == plan : 
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <= 0 or nx > 5 or ny <= 0 or ny>5 : 
        continue
    print(ny, nx)
    x, y = nx, ny
print(y, x)
