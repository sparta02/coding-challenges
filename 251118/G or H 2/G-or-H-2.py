n = int(input())
people = [list(input().split()) for _ in range(n)]
for i in range(len(people)):
    people[i][0]=int(people[i][0])


# Please write your code here.

people.sort(key=lambda x: x[0])

result=0

for i in range(len(people)):
    for j in range(i+1, len(people)):
        temp_G=0
        temp_H=0
        temp=0
        for k in range(i, j+1):
            if people[k][1]=="G":
                temp_G+=1
            elif people[k][1]=="H":
                temp_H+=1
        #print(people[i:j+1], temp_G, temp_H, people[j][0],people[i][0])
        if temp_G==temp_H or temp_G==0 or temp_H==0:
            temp=people[j][0]-people[i][0]
        result=max(result,temp)

if len(people)==1:
    result=0

print(result)


