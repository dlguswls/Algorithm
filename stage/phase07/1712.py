import sys
a, b, c = map(int, sys.stdin.readline().split())
if b>=c : 
    print(-1)
else : 
    # c * cnt > b * cnt + a
    print(int((a/(c-b))+1))