word = input().lower()
unique_word = list(set(word))
cnt = []
for i in unique_word : 
    cnt.append(word.count(i)) 
if cnt.count(max(cnt))>=2 : 
    print('?')
else : 
    print(unique_word[cnt.index(max(cnt))].upper())