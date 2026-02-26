n=int(input())
arr=list(map(int, input().split()))
x, y=0,0
l=0
r=n-1

result=10**20
while(l<r):
    temp=arr[l]+arr[r]

    if abs(temp)<abs(result):
        x=arr[l]
        y=arr[r]
        result=temp

    if temp==0:
        break
    if temp>0:
        r-=1
    if temp<0:
        l+=1

print(x,y)
