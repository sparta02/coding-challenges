n=int(input())
arr=list(map(int, input().split()))

arr.sort()

arr1=[]
arr2=[]

for i in range(n):
    if arr[i]<=0:
        arr1.append(-arr[i])
    else:
        arr2.append(arr[i])
arr1.sort()
# print(arr1)
# print(arr2)
n1=len(arr1)
n2=len(arr2)
result=[]
i=-1
j=-1
for num in range(0, n+1):
    while i<n1-1 and num>arr1[i+1]:
        i+=1
    while j<n2-1 and num>=arr2[j+1]:
        j+=1
    # print(num, i)
    # print(num, j)
    first=i+1
    second=n2-1-j
    # print(f"first:{first}, second: {second}")
    if first+second==num:
        # print(f"{num} ok")
        result.append(num)
    # print()

print(len(result))
print(*result)
# # 이하
# # num 미만인 숫자 중 가장 오른쪽
# # 다음 숫자가 num 이상일 때까지 이동
# # 다음 숫자가 num 미만이면 이동
# [1, 1, 2, 4]
# 거짓말 = 0명
# 참 참 참 참

# 거짓말 = 1명
# 참 참 참 참

# 거짓말 = 2명
# 거짓 거짓 참 참

# 거짓말 = 3명
# 거짓 거짓 거짓 참

# # 이상
# # n 이하인 숫자 중 가장 오른쪽
# # 다음 숫자가 num 초과일 때까지 이동
# # 다음 숫자가 num 이하면 이동
# [0, 1, 1, 2, 4]
# 거짓말 = 0명
# 참 거짓 거짓 거짓 거짓

# 거짓말 = 1명
# 참 참 참 거짓 거짓

# 거짓말 = 2명
# 참 참 참 거짓

# 거짓말 = 3명
# 참 참 참 거짓


# [-2, -1, 0, 1, 2]

# 거짓말 = 0명
# 참 참 참 거짓 거짓

# 거짓말 = 1명