from itertools import combinations
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

arr=[i for i in range(1, n)]

partition_arrs = list(combinations(arr, m-1))
partition_arrs2=[]
for par in partition_arrs:
    par=[0]+list(par)
    par.append(n)
    partition_arrs2.append(par)
#print(partition_arrs2)

result=9999999

for part in partition_arrs2:  
    max_num=0
    #print(part)
    for j in range(len(part)-1):
        temp=0
        #print(j)
        for k in range(part[j], part[j+1]):
            
            temp+=a[k]
            #print(a[k],temp)
        max_num=max(max_num, temp)
    result=min(result,max_num)

print(result)
    