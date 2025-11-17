n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max=0
for i in range(len(price)):
    for j in range(i):
        if price[i]-price[j]>max:
            max=price[i]-price[j]

print(max)