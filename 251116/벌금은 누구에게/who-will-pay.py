N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

arr=[0]*(N+1)

for stu in student:
    arr[stu]+=1

    if arr[stu]>=K:
        print(stu)
        break
else:
    print(-1)