N = int(input())
seat = list(input())
# Please write your code here.

result=0
# i, j 2개의 자리에 새로운 학생 배정
for i in range(N):
    for j in range(i+1, N):
        if seat[i]=="1" or seat[j]=="1":
            continue
        temp_arr=seat[:]
        temp_arr[i]="1"
        temp_arr[j]="1"

        index=-1 # 0~N-1 자리를 탐색하며 가장 최근에 확인한 1의 위치
        dist=999 # 가장 가까운 두 사람의 거리
        for k in range(N):
            if temp_arr[k]=="1":
                if index==-1:
                    index=k
                else:
                    dist=min(dist, k-index)
                    index=k
        result=max(result, dist)

print(result)

