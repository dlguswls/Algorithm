import sys
import itertools  # 순열, 조합 구현

n = int(sys.stdin.readline())
arr = [x for x in range(1, n+1)]
nPr = itertools.permutations(arr, n)
nPr = list(nPr)

def isStackSequence(nums):
    count = 1
    s = []
    for i in nums:
        while count <= i:
            s.append(count)
            count += 1
        if s[-1] == i:
            s.pop()
        else:
            return False
    return True

for i in nPr:
    k = list(i)
    if isStackSequence(k):
        k = map(str, k)
        print(' '.join(k))
