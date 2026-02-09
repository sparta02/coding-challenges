n=int(input())

arr_zero=[0]*41
arr_zero[0]=1
for i in range(2, 41):
    arr_zero[i]=arr_zero[i-1]+arr_zero[i-2]


arr_one=[0]*41
arr_one[1]=1
for i in range(2, 41):
    arr_one[i]=arr_one[i-1]+arr_one[i-2]

# print(arr_zero)
# print(arr_one)


for _ in range(n):
    num=int(input())
    print(arr_zero[num], arr_one[num])
