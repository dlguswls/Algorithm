import sys
from ast import literal_eval
input = sys.stdin.readline
relationships = literal_eval(input())
target = int(input().strip())
limit = int(input().strip())

best = 0
friends = []
friend_ind = []
for i in range(len(relationships)):
    relation = relationships[i]
    if target in relation:
        best += 1
        friend_ind.append(i)
        relation.remove(target)
        friends.append(relation[0])
limit -= 1
just = 0
while limit:
    limit -= 1
    just_friends = []
    for i in range(len(relationships)):
        if i in friend_ind:
            continue
        relation = relationships[i]
        for friend in friends:
            if friend in relation:
                just += 1
                friend_ind.append(i)
                relation.remove(friend)
                just_friends.append(relation[0])
    friends = just_friends

answer = best * 5 + just * 10 + just
print(answer)
