n = int(input())

# Please write your code here.
temp=0
for i in range(n):
    for j in range(n):
        print(temp+1, end=" ")
        temp=(temp+1)%9
    print()