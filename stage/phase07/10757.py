a,b = map(int,input().split())
print(a+b)
## 파이썬은 괜찮은데 C언어는 메모리에 못 담아서 나온 문제!
## 파이썬 메모리 방식 - arbitrary precision
## arbitrary precision : 현재 가용 메모리 모두 수 표현에 끌어 쓸 수 있는 형태
## fixed-precision : 사용할 수 있는 메모리양이 정해져 있음 