import sys
# n = int(sys.stdin.readline().strip())

# h = 0
# m = 0
# s = 0

# cnt = 0
# while h <= n : 
#     if s < 59 : 
#         s += 1
#     else : 
#         if m < 59 : 
#             m += 1
#             s = 0
#         else : 
#             h += 1
#             m = 0
#             s = 0

#     if '3' in str(h) or '3' in str(m) or '3' in str(s) : 
#         cnt += 1
#         print(h,'시 ', m, '분 ', s, '초')
# print(cnt)

import sys
h = int(sys.stdin.readline().strip())

cnt = 0
for i in range(h+1) : 
    for j in range(60) : 
        for k in range(60) : 
            if '3' in str(i) + str(j) + str(k) : 
                cnt += 1
print(cnt)  