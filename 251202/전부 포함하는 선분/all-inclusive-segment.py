n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
a=[ item[0] for item in segments]
b=[ item[1] for item in segments]
# Please write your code here.

result=9999999999999999
for i in range(n):
    temp_a=a[:]
    temp_a.remove(a[i])
    temp_b=b[:]
    temp_b.remove(b[i])

    dist=max(temp_a+temp_b)-min(temp_a+temp_b)
    # print(temp_a)
    # print(temp_b)
    # print(dist)
    result = min(result, dist)
print(result)
    
    