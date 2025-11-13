n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
sum=A[m-1]

while(m!=1):
    if m%2==0:
        m=int(m/2)
    else:
        m-=1
    sum+=A[m-1]

print(sum)