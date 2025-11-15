n = int(input())
name = []
korean = []
english = []
math = []

arr= [tuple(input().split()) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[2], x[3]))
for i in range(n):
    print(arr[i][0], arr[i][1], arr[i][2], arr[i][3])