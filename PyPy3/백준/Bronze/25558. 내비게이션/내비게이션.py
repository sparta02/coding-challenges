t=int(input())
start_x, start_y, end_x, end_y=map(int, input().split())
dist=[]
for _ in range(t):
    m= int(input())
    arr= [[start_x, start_y]]+ [list(map(int, input().split())) for _ in range(m)]+[[end_x, end_y]]
    # print(arr)
    temp=0
    for i in range(m+1):
        temp+=abs(arr[i][0]-arr[i+1][0])
        temp+=abs(arr[i][1]-arr[i+1][1])
    dist.append(temp)

print(dist.index(min(dist))+1)