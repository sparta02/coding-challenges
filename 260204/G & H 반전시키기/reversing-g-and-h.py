N = int(input())
a = input()
b = input()

# Please write your code here.
리스트=[0]*N

for i in range(N):
    if a[i]!=b[i]:
        리스트[i]=1

# print(리스트)

result=0
find=0
for i in range(N):
    if find==0 and 리스트[i]==1:
        find=1
        result+=1
    elif 리스트[i]==0:
        find=0
print(result)
