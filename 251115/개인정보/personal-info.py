n = 5

arr=[input().split() for _ in range(n)]

# Please write your code here.
print("name")
arr.sort(lambda x: x[0])
for i in range(n):
    print(arr[i][0], arr[i][1], arr[i][2])
print()
print("height")
arr.sort(lambda x: -int(x[1]))
for i in range(n):
    print(arr[i][0], arr[i][1], arr[i][2])