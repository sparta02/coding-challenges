n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

i,j = 0, 0

result=0
for i in range(n-1):
    if j<i:
        j=i
    #print(i, j)
    while j+1<n and price[i]<=price[j+1]:
        j+=1
    #print(i, j, j-i)
    result=max(result, price[j]-price[i])

print(result)
