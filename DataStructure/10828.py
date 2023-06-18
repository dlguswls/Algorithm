# # 시간 초과
# N = int(input())  # 명령의 수
# stack_list = []
# answer = []
# for i in range(N):
#     command = input().split()
#     if command[0] == 'push':
#         stack_list.append(command[1])
#     elif command[0] == 'top':
#         if len(stack_list) == 0:
#             answer.append(-1)
#         else :
#             answer.append(stack_list[-1])
#     elif command[0] == 'pop':
#         if len(stack_list) == 0:
#             answer.append(-1)
#         else :
#             answer.append(stack_list.pop())
#     elif command[0] == 'size':
#         answer.append(len(stack_list))
#     else :
#         if len(stack_list) == 0:
#             answer.append(1)
#         else :
#             answer.append(0)
#
# for i in answer:
#     print(i)


# 와우.. sys.stdin.readline()의 중요성!!! 이거 하나로 시간 초과 해결!!!
import sys
N = int(sys.stdin.readline())  # 명령의 수
stack_list = []
answer = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack_list.append(command[1])
    elif command[0] == 'top':
        if len(stack_list) == 0:
            answer.append(-1)
        else :
            answer.append(stack_list[-1])
    elif command[0] == 'pop':
        if len(stack_list) == 0:
            answer.append(-1)
        else :
            answer.append(stack_list.pop())
    elif command[0] == 'size':
        answer.append(len(stack_list))
    else :
        if len(stack_list) == 0:
            answer.append(1)
        else :
            answer.append(0)

for i in answer:
    print(i)


