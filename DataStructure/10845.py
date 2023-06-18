import sys
N = int(sys.stdin.readline())  # 명령의 수
queue_list = []
answer = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue_list.append(command[1])
    elif command[0] == 'front':
        if len(queue_list) == 0:
            answer.append(-1)
        else:
            answer.append(queue_list[0])
    elif command[0] == 'back':
        if len(queue_list) == 0:
            answer.append(-1)
        else :
            answer.append(queue_list[-1])
    elif command[0] == 'pop':
        if len(queue_list) == 0:
            answer.append(-1)
        else :
            answer.append(queue_list[0])
            del queue_list[0]
    elif command[0] == 'size':
        answer.append(len(queue_list))
    else:
        if len(queue_list) == 0:
            answer.append(1)
        else :
            answer.append(0)

for i in answer:
    print(i)