A = input()

# Please write your code here.
sum=0

for i in range(len(A)):
    if A[i]=='(':
        sum+=A[i+1:].count(')')
print(sum)