N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.

# 최종적으로 출력할 값
result=9999999999

# 범위를 i~i+17
for i in range(min(heights), max(heights)+1):
    temp_sum=0
    #print(f"i값:{i}")
    for j in range(N):
        if heights[j]<i:
            #print(heights[j])
            temp_sum+=(heights[j]-i)**2
        if heights[j]>i+17:
            #print(heights[j])
            temp_sum+=(heights[j]-(i+17))**2
    result=min(result, temp_sum)

print(result)

