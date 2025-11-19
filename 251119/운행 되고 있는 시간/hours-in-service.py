n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.

max_x=0

for i in range(len(a)):
    arr=[0]*1001
    for j in range(len(a)):
        if i==j:
            continue
        
        for k in range(a[j], b[j]):
            arr[k]=1
        #print(arr[0:10])
    temp_count=sum(arr)
    max_x=max(max_x, temp_count)

print(max_x)
