n=int(input())
nodes=[[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, v=map(int, input().split())
    nodes[parent].append((child, v))
    nodes[child].append((parent, v))

# 노드 1번에서 가장 먼 노드 찾기
dist=[-1]*(n+1)

stack=[]
stack.append(1)
dist[1]=0

while(stack):
    curr=stack.pop()
    for next_node, distance in nodes[curr]:
        if dist[next_node]==-1:
            dist[next_node]=dist[curr]+distance
            stack.append(next_node)

#가장 멀리있는 노드 번호
select_node=dist.index(max(dist))

#가장 멀리 있는 노드에서 가장 먼 노드 길이

dist=[-1]*(n+1)

stack=[]
stack.append(select_node)
dist[select_node]=0

while(stack):
    curr=stack.pop()
    for next_node, distance in nodes[curr]:
        if dist[next_node]==-1:
            dist[next_node]=dist[curr]+distance
            stack.append(next_node)

print(max(dist))