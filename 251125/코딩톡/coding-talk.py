n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.
arr=[ chr(65+i) for i in range(n)]
#print(arr)
arr.remove(c[p-1])
for i in range(p, m):
    if c[i] in arr:
        arr.remove(c[i])
    #print(c[i], u[i])

if u[p-1]!=0:
    for i in range(len(arr)):
        print(arr[i], end=" ")
