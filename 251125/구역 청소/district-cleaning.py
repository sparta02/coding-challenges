a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

arr=[0]*(max(b,d)+1)

for i in range(a, b):
    arr[i]=1
#print(arr)
for i in range(c, d):
    arr[i]=1
#print(arr)

print(arr.count(1))