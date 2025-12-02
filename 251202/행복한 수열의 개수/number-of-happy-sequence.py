n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]



# 1. 특정 행 or 열이 행복한 수열인지 확인하는 check_happy 함수
def check_happy(arr):
    result=1
    temp=1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            temp+=1
        else:
            temp=1
        result=max(result, temp)
        # print(temp)
    return result


# 2. 행, 열들을 check_happy 함수에 넣는 main 코드

count=0

# 2-1. 행
for i in range(n):
    # temp_arr에 각 행을 저장
    temp_arr=grid[i]
    # 만약 연속된 수가 m개 이상이라면 count+=1
    if check_happy(temp_arr) >=m:
        count+=1

# 2-2. 열
for i in range(n):
    #temp_arr에 각 열을 저장
    temp_arr=[]
    for j in range(n):
        temp_arr.append(grid[j][i])
    # 만약 연속된 수가 m개 이상이라면 count+=1
    if check_happy(temp_arr) >=m:
        count+=1

print(count)