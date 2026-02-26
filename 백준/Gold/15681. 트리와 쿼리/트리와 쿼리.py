import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
n, root, e= map(int, input().split())

# 하위 노드의 갯수를 저장하는 배열
result_nodes= [-1]*(n+1)

edges=[ [] for _ in range(n+1) ]

for _ in range(n-1):
    start, end= map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

find_list=[]


# print(edges)
# print(find_list)

visited=[0]*(n+1)

visited[root]=1

# node의 자식 수를 계산
def calc_child(node):
    # print(f"curr:{node}")
    visited[node]=1
    
    # 내가 루트가 아니고
    # 연결된 edge가 1개라면
    # 1 저장 후 반환
    if node!=root and len(edges[node])==1:
        result_nodes[node]=1
        return 1
    
    childs= edges[node]
    temp=1
    for next in childs:
        if visited[next]==0:
            temp+=calc_child(next)
    result_nodes[node]=temp
    return temp


calc_child(root)

for _ in range(e):
    temp=int(input())
    print(result_nodes[temp])