# 카드 역배치
### a = [1, 2, 3, 4] 일 때 a[ : :-1] = [4, 3, 2, 1]

card = [i for i in range(1, 21)]

import sys
input = sys.stdin.readline

for k in range(10):
    a1, a2 = map(int, input().split())
    card1 = card[:a1-1]
    card2 = card[a1-1:a2][::-1]
    card3 = card[a2:]
    card = card1 + card2 + card3

for i in card:
    print(i, end = ' ')