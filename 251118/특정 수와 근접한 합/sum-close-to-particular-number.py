N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result=99999999999999999999

for i in range(N):
    for j in range(i+1, N):
        if abs(S-(sum(arr)-arr[i]-arr[j]))<result:
            result=abs(S-(sum(arr)-arr[i]-arr[j]))


print(result)

    