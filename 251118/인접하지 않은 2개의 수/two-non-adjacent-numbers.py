n = int(input())
numbers = list(map(int, input().split()))
max=0
# Please write your code here.
for i in range (0, n-2):
    for j in range(i+2,n):
        if numbers[i]+numbers[j]>max:
            max=numbers[i]+numbers[j]

print(max)