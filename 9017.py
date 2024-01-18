import sys

# T = int(sys.stdin.readline().strip())
# N = int(sys.stdin.readline().strip())
teams = list(map(int, sys.stdin.readline().strip().split()))
team = set(teams)
for i in team : 
    if teams.count(i) != 6 : 
        while i in teams : 
            teams.remove(i)
team = set(teams)
v = [[i, value] for i, value in enumerate(teams)]
result = {}
for t in team : 
    cnt = 0
    i = 0
    f = 0
    for k in v : 
        if (i < 4) and (k[0] == t) : 
            cnt += k[1]
            i += 1
        elif (i == 4) and (k[0] == t) : 
            f = k[1]
    result[t] = [cnt, f]
result.sort(key = lambda x : x[1])
print(result)