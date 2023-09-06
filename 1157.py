import sys
s = sys.stdin.readline().strip().upper()
from collections import Counter
counter = Counter(s)
s_sort = sorted(counter.items(), key = lambda x : x[1], reverse = True)
if len(s_sort) == 1 : 
    print(s_sort[0][0])
elif s_sort[0][1] == s_sort[1][1] : 
    print("?")
else : 
    print(s_sort[0][0])