A=list(input())
B=list(input())

arr=[0]*100

for i in A:
    arr[ord(i)-65]+=1
for i in B:
    arr[ord(i)-65]-=1

result=0

for i in arr:
    result+=abs(i)

print(result)