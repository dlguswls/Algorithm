# 남학생 : 자신이 받은 숫자의 배수인 스위치의 상태 바꾸기
# 여학생 : 자신이 받은 숫자로부터 대칭이 가장 큰 범위의 모든 스위치 상태 바꾸기

import sys

N = int(sys.stdin.readline().strip())
switch = list(map(int, sys.stdin.readline().strip().split(' ')))
student = int(sys.stdin.readline().strip())

for i in range(student) : 
    sex, number = map(int, sys.stdin.readline().strip().split())
    if sex == 1 : # 남학생
        cnt = number
        while number <= N : 
            if switch[number-1] == 0 : 
                switch[number-1] = 1
            else : 
                switch[number-1] = 0
            number += cnt
    else : # 여학생
        first_index = number-2
        last_index = number
        while first_index >=0 and last_index+1 <= N and switch[first_index] == switch[last_index] : 
            first_index -= 1
            last_index += 1
        for i in range(first_index+1, last_index) : 
            if switch[i] == 0 : 
                switch[i] = 1
            else : 
                switch[i] = 0

for i in range(len(switch)) : 
    print(switch[i], end = ' ')
    if (i+1) % 20 == 0 : 
        print()