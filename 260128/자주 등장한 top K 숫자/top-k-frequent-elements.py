n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
count_list=[0]*100001

for i in range(n):
    count_list[arr[i]]+=1

new_list=[]
for i in range(100001):
    if count_list[i]!=0:
        new_list.append((i, count_list[i]))

new_list=sorted(new_list, key=lambda x: (-x[1],-x[0]))

for i in range(k):
    print(new_list[i][0], end=" ")