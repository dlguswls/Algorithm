import sys

N, G = sys.stdin.readline().strip().split()
name = []

for i in range(int(N)) : 
    n = sys.stdin.readline().strip()
    name.append(n)

name = set(name)

if G == 'Y' : 
    ans = len(name) // 1
elif G == 'F' : 
    ans = len(name) // 2
else : 
    ans = len(name) // 3
    
print(ans)

## 검색
import sys
input = sys.stdin.readline
dict = {"Y":2,"F":3,"O":4}
a,b=map(str,input().split())
ans=set([])
y = dict[b]-1
for i in range(int(a)):
    ans.add(input().rstrip())
print(len(ans)//y)