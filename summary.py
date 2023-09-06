# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 0]
print(array)
## 리스트 초기화를 할 때는 리스트 컴프리헨션 사용해야 함! 그렇지 않으면 의도치 않은 결과가 출력될 수 있음
n = 3
m = 4
array = [[0]*m]*n
print(array)
array[1][1] = 5
print(array)   # [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
array =  [[0] * m for _ in range(n)]
print(array)
array[1][1] = 5
print(array)   # [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]

# 리스트 메서드
a = [1, 4, 3]
print("기본 리스트 : ", a)
a.append(2)
print("삽입 : ", a)
a.sort()
print("오름차순 정렬 : ", a)  # 원본 리스트 변경함, 내림차순 정렬 원할 때는 "reverse = True" 추가
a.reverse()
print("원소 뒤집기 : ", a)
a.insert(2, 3)
print("인덱스 2에 3 추가 : ", a)
print("특정 요소의 개수 세기 : ", a.count(3))
a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

# 집합 자료형
data = set([1, 2, 3])  # 또는 data = {1, 2, 3}
data.add(4)  # 새로운 원소 추가
data.update([5, 6])  # 새로운 원소 여러 개 추가
data.remove(3)   # 특정한 값 갖는 원소 삭제
data.discard(3)  # data에 3 원소가 없을 때 실행해도 오류 X

# global
a = 0
def func() : 
    global a
    a += 1
for i in range(10) :
    func()
print(a)

# 람다 표현식
print((lambda a, b : a+b)(3, 7))

# 데이터 입력
import sys
data = sys.stdin.readline().rstrip()  # input() 대신 사용하기!
print(data)

# 내장함수 : sum, min, max, sorted
print( sorted([9,1,5,4]) )
print( sorted( [('홍길동', 35), ('이순신', 75), ('이무개', 50)], key = lambda x : x[1], reverse = True ) )

# itertools : 파이썬에서 반복 데이터 처리 기능을 포함한 라이브러리
## permutations : iterable객체에서 r개의 데이터 뽑아 일렬로 나열하는 모든 경우의 수(순열)
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
## combinations : iterable 객체에서 r개의 데이터를 뽑아 순서 고려하지 않고 나열하는 모든 경우(조합)
from itertools import combinations
result = list(combinations(data, 2))
print(result)
## product : permutations와 같지만 중복 허용
from itertools import product
result = list(product(data, repeat = 2))  # 얘만 repeat 필요!
print(result)
## combinations_with_replacement : combinations와 같지만 중복 허용
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)

# heapq : 우선순위 큐 기능 구현에 활용
import heapq
def heapsort(iterable) : 
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value) # 순서 상관 없이 원소 삽입
    for value in range(len(h)) : 
        result.append(heapq.heappop(h))  # 최소 힙으로, 가장 작은 원소부터 반환(h에서 제거하면서 반환)
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])    ## heapq.heapify(리스트) : 이미 생성해둔 자료형 변경 가능
print(result)
## 파이썬은 최대 힙을 제공하지 않기 때문에 최대 힙을 구현하기 위해서는 음수 이용하기
## heapq.value(h, -value), result.append(-heapq.heappp(h))

# bisect : 이진탐색 구현 라이브러리
## bisect_left : 정렬 순서 유지하면서 리스트 a에 x를 삽입할 가장 왼쪽 인덱스 찾기
## bisect_right : 정렬 순서 유지하면서 리스트 a에 x를 삽입할 가장 오른쪽 인덱스 찾기
## ex] a = [1,2,4,4,8]에서 bisect_left(a, 4)는 2, bisect_right(a, 4)는 4반환
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, 4))
print(bisect_right(a, 4))
## 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구할 때 효과적
def count_by_range(a, left_value, right_value): 
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print("값이 4인 데이터 개수 출력 : ", count_by_range(a, 4, 4))
print("값이 [-1, 3] 범위에 있는 데이터 개수 출력 : ", count_by_range(a, -1, 3))

# deque : 스택(후입선출 : LIFO) or 큐(선입선출 : FIFO) 자료구조 대용
## 리스트 자료형과 달리 인덱싱, 슬라이싱 등의 기능 불가
## 연속적으로 나열된 데이터의 시작부분이나 끝부분에 데이터를 삽입하거나 삭제할 때 효과적
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

# Counter : iterable 객체의 원소가 몇 번 등장했는지 출력
from collections import Counter
counter = Counter(['red','blue','red','green','blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# math : 수학 기능 포함
import math
print(math.factorial(5))   # 팩토리얼
print(math.sqrt(7))  # 제곱근
print(math.gcd(21, 14))  # 최대공약수
print(math.pi)
print(math.e)  # 자연상수 e