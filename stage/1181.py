# sort의 key 옵션에 지정된 함수의 결과에 따라 정렬
# 리스트.sort()는 원본 변형, sorted(리스트)는 원본 그대로고 정렬된 결과값 반환
N = int(input())
word_lists = [input() for _ in range(N)]
word_lists = list(set(word_lists))
word_lists.sort()
word_lists.sort(key = len)
for i in word_lists :
    print(i)


