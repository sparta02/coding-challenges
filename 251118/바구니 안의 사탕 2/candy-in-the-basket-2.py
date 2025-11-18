N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

#0 1 2 3 4 5 ... 12 13 14 15
result=0
for i in range(K,max(pos)+1-K):
    temp=0
    for j in range(len(candy)):
        if i-K<=pos[j]<=i+K:
            temp+=candy[j]
    result=max(result, temp)

if c<=K:
    result=sum(candy)
print(result)