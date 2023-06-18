import numpy as np
from collections import Counter
# N = int(input())
# nums = []
# for i in range(N) :
#     nums.append(int(input()))

# print(sum(nums))
# print(np.median(nums))
#
# print(max(nums)-min(nums))

a = [1,2,3,4,4]
print(np.median(a))
print(max(a))
cnt = Counter(a)
print(cnt.most_common(1))