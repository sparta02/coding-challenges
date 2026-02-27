n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

uf=[i for i in range(n+1)]
# print(uf)

# x의 root ㅊ
def find(x):
    if uf[x]==x:
        return x
    root = find(uf[x])
    uf[x]=root
    return root

# a가 포함된 집합과 b가 포함된 집합 합치기
def union(a, b):
    root_a=find(a)
    root_b=find(b)

    uf[root_a]=root_b

for t, a, b in query:
    if t==0:
        union(a, b)
    else:
        if find(a)==find(b):
            print(1)
        else:
            print(0)