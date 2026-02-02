word = input()

# Please write your code here.
i=0
j=0
result=0

maps={}

for i in range(len(word)):
    # 동일한 문자가 2번 나오기 전까지 j 이동
    while j<len(word) and word[j] not in maps:
        maps[word[j]]=1
        j+=1
    
    #print(i, j)
    result=max(result, j-i)
    maps.pop(word[i])

print(result)