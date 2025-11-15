n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr=[0 for i in range(2000)]
현재 = 1000

def cal(i,j):
    global arr
    global 현재
    #print(현재-15, i)
    if j =="R":
        for k in range(현재, 현재+i):
            arr[k]+=1
        현재+=i
    elif j=="L":
        for k in range(현재-i, 현재):
            arr[k]+=1
        현재-=i
    #print(arr)

for i in range(n):
    cal(x[i], dir[i])
    

cnt=0
for i in range(2000):
    if arr[i]>=2:
        cnt+=1
print(cnt)


