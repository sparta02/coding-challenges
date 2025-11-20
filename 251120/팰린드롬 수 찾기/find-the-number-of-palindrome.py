X, Y = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(X, Y+1):
    temp=list(str(i))
    temp2=temp[:]
    temp2.reverse()
    if temp == temp2: 
        cnt+=1
print(cnt)