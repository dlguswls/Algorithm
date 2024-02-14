# 단어 순서 우선순위
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# M보다 짧은 길이의 단어는 포함 X

import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split()) # 단어 개수 N, 최소 단어길이 M
words = [] # 외울 단어들
for i in range(N) : 
    word = sys.stdin.readline().strip()
    if len(word) >= M : 
        words.append(word)

counter = Counter(words)

word_info = {}
for i in counter : 
    word_info[i] = [counter[i], len(i), i]

word_info = sorted(word_info.items(), key = lambda x : (-x[1][0], -x[1][1], x[1][2]))

for key, value in word_info : 
    print(key)


