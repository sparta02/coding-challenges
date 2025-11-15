n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

arr=[[0,0,-1] for i in range(200000)]
현재=int(len(arr)/2)
def cal(steps, way):
    global arr
    global 현재

    if way=="R":
        for i in range(현재, 현재+steps):
            arr[i][0]+=1
            arr[i][2]=0
        현재+=(steps-1)
    else:
        for i in range(현재-steps+1, 현재+1):
            arr[i][1]+=1
            arr[i][2]=1
        현재-=(steps-1)


for i in range(n):
    cal(x[i], dir[i])

white=0
black=0
for ar in arr:
    if ar[0]>=1 and ar[2]==0:
        black+=1
    elif ar[1]>=1 and ar[2]==1:
        white+=1

print(white, black)
