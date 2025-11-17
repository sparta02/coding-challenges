n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_dist=9999999999999999999999999999

for i in range(n):
    temp=0
    for j in range(n):
        temp+=abs(i-j)*A[j]
    if min_dist>temp:
        min_dist=temp

print(min_dist)