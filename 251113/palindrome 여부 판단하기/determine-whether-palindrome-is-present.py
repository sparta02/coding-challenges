A = input()

# Please write your code here.
a=int(len(A)/2)
check=0
for i in range(a):
    if A[i]!=A[len(A)-1-i]:
        check=1

if check:
    print("No")
else:
    print("Yes")