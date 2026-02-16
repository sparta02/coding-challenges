n, k=map(int, input().split())

arr=[]

for _ in range(n):
    arr.append(int(input()))

result=0
for coin in arr[::-1]:
    result+=k//coin
    k%=coin

print(result)