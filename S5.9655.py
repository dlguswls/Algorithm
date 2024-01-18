import sys
import random

N = int(sys.stdin.readline().strip())
choice_list = [1, 3]
cnt = 0
while N>0 : 
    choice = random.choice(choice_list)
    N -= choice
    cnt += 1
if cnt % 2 == 0 : 
    print("CY")
else : 
    print("SK")