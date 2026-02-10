n, m = map(int, input().split())
arr= [ [0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1]=1
    arr[b-1][a-1]=1

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end=" ")
#     print()
# print()

visited=[0]*n

def dfs(num):
    stack=[]
    stack.append(num)
    visited[num]=1
    while(stack):
        curr=stack.pop()
        for i in range(n):
            if i==curr:
                continue
            if arr[curr][i]==1 and visited[i]==0:
                stack.append(i)
                #print(i)
                visited[i]=1


result=0
for i in range(n):
    if visited[i]==0:
        #print(i)
        dfs(i)
        result+=1
        # print(result)
        # print("========")

print(result)
