games, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(games)]

# Please write your code here.
cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            continue
        temp=True
        for k in range(games):
            if arr[k].index(i)<arr[k].index(j):
                temp=False
        if temp:
            cnt+=1
print(cnt)
