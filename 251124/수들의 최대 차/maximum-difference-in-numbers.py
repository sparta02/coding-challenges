from itertools import combinations

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

result=0 # 반복문을 돌며 갱신하여 최종적으로 출력할 수

for i in range(1, N+1): # 1~N개를 고르기
    temp_arr=list(combinations(arr, i))

    for item in temp_arr: # 임시로 만든 temp_arr 내의 list들 체크
        max_num=max(item)
        min_num=min(item)
        if max_num-min_num<=K: # 최대값 - 최소값이 K 이하라면
            result=max(result, len(item))

print(result)