from itertools import permutations

n = int(input())

# Please write your code here.

result_list=list(permutations(range(1, n+1), n))

for hi in result_list:
    for j in range(n):
        print(hi[j], end=" ")
    print()