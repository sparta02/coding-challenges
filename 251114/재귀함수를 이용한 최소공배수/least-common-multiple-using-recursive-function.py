n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def cal(a, b):
    i=1
    while True:
        if (a*i)%b==0:
            break
        else:
            i+=1
    return a*i

for i in range(len(arr)-1):
    result=cal(arr[i], arr[i+1])
    arr[i+1]=result
print(arr[len(arr)-1])