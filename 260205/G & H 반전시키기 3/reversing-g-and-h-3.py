N = int(input())
a = list(input())
b = list(input())

# Please write your code here.

compare=[]

for i in range(N):
    if a[i]==b[i]:
        compare[i]=0
    else:
        compare[i]=1

print(compare)