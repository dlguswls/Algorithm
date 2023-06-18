h, m = map(int,input().split())
l = int(input())
m2 = m+l
while m2>=60 : 
    h += 1
    if h>23 : 
        h-=24
    m2 = m2-60
print(h, m2)
