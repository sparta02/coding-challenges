n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
maps={}

for i in range(n):
    temp_str="".join((sorted(words[i])))
    maps[temp_str]=maps.get(temp_str,0)+1

result=max([x for x in maps.values()])
print(result)