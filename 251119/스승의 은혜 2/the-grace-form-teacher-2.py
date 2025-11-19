from itertools import combinations
N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
P.sort()
result=0

for i in range(1,N+1):
    temp=sum(P[:i])-int(P[i-1]/2)
    if B>=temp:
        result=max(result, i)
print(result)
    
