import sys

N = int(sys.stdin.readline().strip())
body = []

for i in range(N) : 
    body.append(sys.stdin.readline().strip())

# 심장
x = 0
y = 0
for i in range(N) : 
    for j in range(N) : 
        if body[i][j] == '*' : 
            x = i+1
            y = j
            break
    if x > 0 : 
        break

print(x+1, y+1)

# 왼쪽 팔
left_arm = 0
for i in range(y) : 
    if body[x][i] == '*' : 
        left_arm += 1

# 오른쪽 팔
right_arm = 0
for i in range(y+1, N) : 
    if body[x][i] == '*' : 
        right_arm += 1

# 허리
waist = 0
for i in range(x+1, N) : 
    if body[i][y] == '_' : 
        waist = i-1-x
        break

# 왼쪽 다리
left_leg = 0
for i in range(x+waist+1,N) : 
    if body[i][y-1] == '*' : 
        left_leg += 1
        
# 오른쪽 다리
right_leg = 0
for i in range(x+waist+1,N) : 
    if body[i][y+1] == '*' : 
        right_leg += 1
    
print(left_arm, right_arm, waist, left_leg, right_leg)