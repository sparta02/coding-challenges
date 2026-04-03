n, k = map(int, input().split())
sign=[list(map(int, input().split())) for _ in range(k)]
sign.sort()
# print(sign)

result=0
curr=0
for i in range(k):
    x, t, k=sign[i]
    result+=(x-curr)
    curr=x

    temp=result
    temp-=k
    temp=temp%(2*t)
    # print(f"temp:{temp}")

    if not 0<=temp<t:
        result+=(2*t-temp)
    # print(result)

result+=n-curr
print(result)

# s<=현재<s+(짝수)t이면
# s+(짝수)t까지 기다려야함

# 0<=현재<t
# 1~2초
# 3~4빨
# 5~6초
