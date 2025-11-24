from itertools import permutations

n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

temp_arr=[i for i in range(1, n+1)]
arr=list(permutations(temp_arr, n))

for items in arr:
    for i in range(n-1):
        if items[i]+items[i+1]!=adjacent[i]:
            break
    else:
        for j in range(n):
            print(items[j], end=" ")
