from itertools import combinations
N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.

result=0
for i in range(1, N):
    arr=list(combinations(P,i))
    for ar in arr:
        for j in range(len(ar)):
            if sum(ar)-int(ar[j]/2)<B:
                result=max(result, len(ar))

print(result)