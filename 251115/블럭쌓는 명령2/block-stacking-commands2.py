n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr=[ 0 for i in range(n+1)]

for com in commands:
    for i in range(com[0], com[1]+1):
        arr[i]+=1

print(max(arr))
