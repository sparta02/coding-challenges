word, k = input().split()
k = int(k)

# Please write your code here.

maps={}
i,j =0,0
result=0

for i in range(len(word)):
    # 1. j가 index를 초과하지 않고
    # 2. 이미 maps에 word[j]가 있거나,
    # 새롭게 추가된다면 기존 길이가 1 이하
    while j<len(word) and (word[j] in maps or len(maps)<k):
        maps[word[j]]=maps.get(word[j],0)+1
        j+=1
    # print(i)
    # print(maps)
    
    result=max(result, j-i)
    temp=maps.pop(word[i])
    if temp>=2:
        maps[word[i]]=temp-1
    

print(result)
