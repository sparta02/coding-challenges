n, m= map(int, input().split())

arr=list(map(int, input().split()))

arr.sort()
visited=[0]*(max(arr)+1)
list=[]
def choose(k):
    if k==m:
        for item in list:
            print(item, end=" ")
        print()
        return
    
    for num in arr:
        if visited[num]==1:
            continue
        visited[num]=1
        list.append(num)
        choose(k+1)
        list.pop()
        visited[num]=0

choose(0)