n, k = map(int, input().split())
arr=[ list(map(int, input().split())) +[1] for _ in range(n)]

for i in range(n):
    if arr[i][0]==k:
        arr[i][-1]=0

arr.sort(key=lambda x:(-x[1], -x[2], -x[3], x[4]))

result=0
for i in range(n):
    if arr[i][0]==k:
        result=i+1
        break

print(result)