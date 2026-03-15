t= int(input())
n=int(input())
list_A=list(map(int, input().split()))
m=int(input())
list_B=list(map(int, input().split()))

# A배열에서 나올 수 있는 모든 값을
# maps에 추가
# B배열에서 나올 수 있는 값들을
# 순회하면서 maps에 있나 보자

sum_A=[]
temp=0
for i in range(n):
    temp+=list_A[i]
    sum_A.append(temp)

# print(sum_A)
maps_A={}

for i in range(n-1, -1, -1):
    maps_A[sum_A[i]]=maps_A.get(sum_A[i], 0)+1
    for j in range(i):
        temp=sum_A[i]-sum_A[j]
        maps_A[temp]=maps_A.get(temp, 0)+1
    
# print(maps_A)

result=0

sum_B=[]
temp=0
for i in range(m):
    temp+=list_B[i]
    sum_B.append(temp)

# print(sum_B)

for i in range(m-1, -1, -1):
    temp=sum_B[i]
    result+=maps_A.get(t-temp, 0)
    for j in range(i):
        temp=sum_B[i]-sum_B[j]
        result+=maps_A.get(t-temp, 0)
    
print(result)
