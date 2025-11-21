arr = [input() for _ in range(3)]

# Please write your code here.

result_arr=[]
for i in range(3):
    x1=set(arr[i])
    if len(x1)==2:
        result_arr.append(list(x1))

for i in range(3):
    x1=[]
    x1.append(arr[0][i])
    x1.append(arr[1][i])
    x1.append(arr[2][i])
    x1=set(x1)
    if len(x1)==2:
        result_arr.append(list(x1))
x1=[]
x1.append(arr[0][0])
x1.append(arr[1][1])
x1.append(arr[2][2])
x1=set(x1)
if len(x1)==2:
    result_arr.append(list(x1))

x1=[]
x1.append(arr[0][2])
x1.append(arr[1][1])
x1.append(arr[2][0])
x1=set(x1)
if len(x1)==2:
    result_arr.append(list(x1))

for i in result_arr:
    i.sort()
arr = {tuple(i) for i in result_arr}
#print(result_arr)
#print(arr)
print(len(arr))