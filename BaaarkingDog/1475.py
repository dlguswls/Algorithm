import sys
input = sys.stdin.readline

n = list(input().strip())
for i in range(len(n)):
    if n[i] == '6':
        n[i] = str(int(n[i]) + 3)
cnt_9 = n.count('9')//2
for i in range(cnt_9):
    n.remove('9')

cnt = 0
while n:
    cnt += 1
    n_li_set = list(set(n))
    for i in n_li_set:
        n.remove(i)

print(cnt)

### 이게 정답...!
word = input()
ans = [0] * 10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1
 
print(max(ans))