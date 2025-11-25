n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

sum_A=0
sum_B=0

for i in range(n):
    sum_A+=A[i]*(n-i)

for i in range(n):
    sum_B+=B[i]*(n-i)

print(sum_A-sum_B)