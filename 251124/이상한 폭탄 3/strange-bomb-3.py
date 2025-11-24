N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

def check_index(n):
    if n<0 or n>=N:
        return False
    return True

result_arr=[]

for i in range(N):
    for j in range(i-K, i+K+1):
        if check_index(j) and num[i]==num[j]:
            result_arr.append(num[i])
            #print(num[i])
            break

value=0
count=0

for i in result_arr:
    temp_count=result_arr.count(i)
    if count<temp_count:
        value=i
        count=temp_count
    if count==temp_count and value<i:
        value=i
        count=temp_count


print(value)

        