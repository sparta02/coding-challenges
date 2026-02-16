n, m = map(int, input().split())
people={}

temp=list(map(int, input().split()))
if temp[0]!=0:
    for i in range(1, len(temp)):
        people[temp[i]]=1

party=[]

for _ in range(m):
    temp=list(map(int, input().split()))
    temp.pop(0)
    party.append(temp)

# print(people.keys())
# print(party)

checked=[]

flag1=-1
flag2=len(people)
while(flag1 != flag2):
    flag1=flag2
    for i in range(m):
        # 아직 해당 파티는 추가되지 않았고
        if i not in checked:
            # 감염자가 1명이라도 있다면
            for person in party[i]:
                if person in people:
                    # 전부 다 감염자로 추가
                    for person in party[i]:
                        people[person]=1
                    checked.append(i)
                    break
    flag2=len(people)
            
# print(people.keys())
# print(checked)

print(m-len(checked))