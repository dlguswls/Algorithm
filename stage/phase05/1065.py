import sys
a = int(sys.stdin.readline())
raw = [num for num in range(1,a+1)]
no_han = []
for n in raw : 
    diff = []
    nn = str(n)
    for i in range(0,len(nn)-1) : 
        diff.append(int(nn[i])-int(nn[i+1])) 
    for i in range(0, len(diff)-1) : 
        if diff[i] != diff[i+1] :
            no_han.append(n)
            break
print(len(set(raw) - set(no_han)))