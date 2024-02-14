import sys
from collections import deque

N = int(sys.stdin.readline().strip())
cards = deque([i+1 for i in range(N)])

while len(cards) > 1 : 
    cards.popleft()
    change = cards.popleft()
    cards.append(change)
print(cards[0])