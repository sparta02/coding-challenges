n,m= map(int, input().split())
result=0
i=0
while n!=1 and m!=1:
    if i==0:
        n-=1
        result+=1
        i=(i+1)%2
    else:
        m-=1
        result+=1
        i=(i+1)%2
    
print(result+1)