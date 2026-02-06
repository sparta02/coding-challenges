n=int(input())
arr=[]
for i in range(n):
    age, name= input().split()
    arr.append([i, int(age), name])
# print(arr)
arr.sort(key=lambda x:(x[1], x[0]))


for i in range(n):
    print(arr[i][1], arr[i][2])
