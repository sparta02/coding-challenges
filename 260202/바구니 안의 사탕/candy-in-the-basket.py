n, k = map(int, input().split())
candy = []
pos = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

maps={}
for i in range(n):
    maps[pos[i]]=maps.get(pos[i], 0)+candy[i]
#print(maps)

# Please write your code here.
i, j = 1, 2*k+1
result=0
temp_sum=0
for k in range(1, 2*k+2):
    if k in maps:
        temp_sum+=maps[k]

result=max(result, temp_sum)

for i in range(1, 20):
    j+=1
    if j in maps:
        temp_sum+=maps[j]
    if i in maps:
        temp_sum-=maps[i]
    i+=1
    #print(i, j)
    result=max(result, temp_sum)
    #print(temp_sum)

print(result)
    
