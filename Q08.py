# import sys
# s = sys.stdin.readline().strip()
# S = []
# N = 0
# for i in s : 
#     if ord(i) > ord('9') : 
#         S.append(i)
#     else : 
#         N += int(i)
# S.sort()
# print(''.join(S)+str(N))

import sys
data = sys.stdin.readline().strip()
S = []
N = 0
for d in data : 
    if d.isalpha() : 
        S.append(d)
    else : 
        N += int(d)
S.sort()
if N != 0 : 
    S.append(str(N))
print(''.join(S))