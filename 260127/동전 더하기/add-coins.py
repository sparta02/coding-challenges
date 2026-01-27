n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
# Please write your code here.

result=0

for coin in coins:
    # print(coin)
    # print(k//coin)
    result+=(k//coin)
    k%=coin

print(result)