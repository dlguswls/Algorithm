h, m = map(int, input().split())
if (m-45)<0 : 
    h = h-1
    if h<0 : 
        h = 24+h
    m = 60+(m-45)
    print(h, m)
else : 
    print(h, m-45)