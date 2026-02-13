n,m =map(int, input().split())

arr=[0]+list(map(int, input().split()))

arr.sort()
# print(arr)
temp=[]
result=[]

def choose(index, k):
    if k==m:
        result.append(tuple(temp))
        return
    
    for i in range(index, n+1):
        temp.append(arr[i])
        choose(i, k+1)
        temp.pop()
    

choose(1, 0)
result=list(set(result))
result.sort()
for row in result:
    for num in row:
        print(num, end=" ")
    print()