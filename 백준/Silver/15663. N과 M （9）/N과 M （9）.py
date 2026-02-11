n, m= map(int, input().split())

arr=list(map(int, input().split()))

arr.sort()

visited=[0]*(n+1)
temp_list=[]
result=[]

def choose(k):
    if k==m:
        result.append((tuple(temp_list)))
        return
    
    for i in range(n):
        if visited[i]==1:
            continue
        visited[i]=1
        temp_list.append(arr[i])
        choose(k+1)
        temp_list.pop()
        visited[i]=0
    
choose(0)
result=list(set(result))
result.sort()

for re in result:
    for i in re:
        print(i, end=" ")
    print()