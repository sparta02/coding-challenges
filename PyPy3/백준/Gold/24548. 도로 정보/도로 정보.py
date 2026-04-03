n=int(input())
road=input()
road=road.replace('T','0')
road=road.replace('G','1')
road=road.replace('F','2')
road=road.replace('P','3')
# print(road)
temp=[0,0,0,0]
# print(temp)
arr=[temp]

for i in range(n):
    num=int(road[i])
    temp=arr[-1][:]
    temp[num]=(temp[num]+1)%3
    arr.append(temp)
# print(arr)

result=0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                temp=arr.count([a,b,c,d])
                if temp>=2:
                    result+=(int(temp*(temp-1)/2))

print(result)
