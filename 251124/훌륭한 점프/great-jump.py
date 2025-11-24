n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def check_stone(check_num):
    temp_arr=[]
    for i, n in enumerate(arr):
        if n<=check_num:
            temp_arr.append(i)
    #print(check_num,temp_arr)
    if 0 not in temp_arr or (n-1) not in temp_arr:
        return False
    # ★ prev를 0번 돌로 맞춰두고 거리 비교 시작
    prev = 0

    for idx in temp_arr:
        if idx - prev > k:  # 다음 밟을 수 있는 돌까지 거리
            return False
        prev = idx

    return True



result=999

for i in range(n, min(arr[0], arr[-1])-1,-1):
    if check_stone(i):
        result=min(result, i)

print(result)