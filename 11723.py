# import sys
# M = int(sys.stdin.readline().strip())

# S = set()
# for i in range(M) : 
#     command = sys.stdin.readline().strip().split()
#     if len(command) == 1 : 
#         if command[0] == 'all' : 
#             S = set([i for i in range(1, 21)])
#         else : 
#             S = set()
#     else : 
#         c = command[0]
#         n = int(command[1])
#         if c == "add" : 
#             S.add(n)
#         elif c == 'remove' : 
#             S.discard(n)
#         elif c == 'check' : 
#             if n in S : 
#                 print(1)
#             else : 
#                 print(0)
#         else :
#             if n in S : 
#                 S.remove(n)
#             else : 
#                 S.add(n)


import sys
result = set()
N = int(sys.stdin.readline().strip())
for _ in range(N) : 
    command = sys.stdin.readline().strip().split()
    if len(command) == 1 : 
        if command[0] == 'all' : 
            result = set([i for i in range(1, 21)])
        elif command[0] == 'empty' : 
            result = set()
    else : 
        cal, num = command
        num = int(num)
        if cal == 'add' : 
            result.add(num)
        elif cal == 'remove' : 
            result.discard(num)
        elif cal == 'check' : 
            if num in result : 
                print(1)
            else : 
                print(0)
        elif cal == 'toggle' : 
            if num in result : 
                result.remove(num)
            else : 
                result.add(num)


# 집합연산에서 .remove(대상)은 지우려는 엘리먼트가 존재하지 않으면 KeyError, .discard(대상)은 정상종료
