# 연결리스트 풀이
class Node:
  def __init__(self, key):
    self.key = key
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def __len__(self):
    return self.size

  def pushFront(self, key):
    new_node = Node(key)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
    return True

  def popFront(self):
    if self.size > 0:
      key = self.head.key
      self.head = self.head.next
      self.size -=1
      return key
    return None

  def remove(self, x): # x노드를 모를 경우 search필요
    if self.size == 0 or x == None:
      return False
    elif x == self.head:
      self.popFront()
      return True
    else:
      prev = self.head
      while prev.next !=x:
        prev = prev.next
      prev.next = x.next
      self.size -= 1
      return True

N, k = map(int, (input().split()))
L = SinglyLinkedList()
for i in range(N, 0, -1):
  L.pushFront(i)

line = []
x = L.head
cnt = 0
while L.size != 0:
  for _ in range(k):
    if L.size == 0:
      break
    cnt +=1
    if cnt == k:
      continue
    x = x.next
    if x == None:
      x = L.head
  L.remove(x)
  line.append(x.key)
  if len(L) == 0:
      break
print('<', end='')
print(*line, sep=', ', end='')
print('>')

# 배열 풀이
N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]  # 맨 처음에 원에 앉아있는 사람들

answer = []  # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
  num += K - 1
  if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
    num = num % len(arr)

  answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')

