import sys
a = sys.stdin.readline()
alphabet = list(range(97, 123))   # 아스키코드로 알파벳 숫자 범위
for x in alphabet : 
    print(a.find(chr(x)), end = ' ')