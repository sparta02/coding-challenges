N = int(input())
a = list(input())
b = list(input())

# Please write your code here.

compare=[]

for i in range(N):
    if a[i]==b[i]:
        compare.append(0)
    else:
        compare.append(1)

result=0
compare2=[]
temp=0
for i in range(N):
    if compare[i]==1:
        temp+=1
    elif compare[i]==0 and temp!=0:
        compare2.append(temp)
        temp=0

# print(compare)
# print(compare2)

for i in range(len(compare2)):
    if compare2[i]<=4:
        result+=1
    else:
        result+=int((compare2[i]+3)//4)
print(result)