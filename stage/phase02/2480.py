a, b, c = map(int, input().split())
if a==b==c : 
    print(10000+a*1000)
elif ((a==b)&(b!=c)) | ((a==c)&(b!=c)) : 
    print(1000+a*100)
elif ((b==c)&(b!=a)) :
    print(1000+b*100)
elif (a!=b)&(a!=c)&(b!=c) : 
    ma = max(a,b)
    ma = max(ma, c)
    print(ma*100)