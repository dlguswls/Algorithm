n = int(input())
cnt = n
for _ in range(n) : 
    word= input()
    for j in range(0, len(word)-2) : 
        if word[j] != word[j+1] :
            new_word = word[j+1:]
            if word[j] not in new_word : 
                pass
            else : 
                cnt -= 1
                break

print(cnt)