str = input()

# Please write your code here.
maps={}

for i in str:
    maps[i]=maps.get(i,0)+1
# print(maps)
result="None"

for key, value in maps.items():
    if value==1:
        result=key
        break

print(result)