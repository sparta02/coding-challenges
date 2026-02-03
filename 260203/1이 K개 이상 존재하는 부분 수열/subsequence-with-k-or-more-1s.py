n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

one_list=[]

for i in range(n):
    if arr[i]==1:
        one_list.append(i)

#print(one_list)

result=9999999

if len(one_list)>=k:
    for i in range(len(one_list)-(k-1)):
        result=min(result, one_list[i+k-1]-one_list[i]+1)
else:
    result=-1

print(result)