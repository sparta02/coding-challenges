n=int(input())
k=int(input())

graph= [ [0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a][b]=1
    graph[b][a]=1

def print_graph():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
    print()

# print_graph()

# 해당 칸이 1이라면 바이러스에 감염된 컴퓨터
visited=[0]*n
visited[0]=1

# dfs로 1번 컴퓨터와 연결된 모든 컴퓨터 방문

stack=[]
stack.append(0)
while(stack):
    curr_com=stack.pop()
    for i in range(n):
        if i==curr_com:
            continue
        if visited[i]==0 and graph[curr_com][i]==1:
            stack.append(i)
            visited[i]=1

print(sum(visited)-1)
