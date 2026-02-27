n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

# Please write your code here.

uf=[ i for i in range(n+1)]

def find(x):
    if uf[x]==x:
        return x
    root=find(uf[x])
    uf[x]=root
    return root

def union(a, b):
    A=find(a)
    B=find(b)
    uf[A]=B

for i in range(m):
    oper=operations[i]
    if oper[0]=='x':
        union(oper[1], oper[2])
    else:
        root=find(oper[1])
        print(uf.count(root))
# print(uf)