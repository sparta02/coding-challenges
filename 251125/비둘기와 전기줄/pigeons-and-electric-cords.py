N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.

arr = [-1]*11

cnt=0 # 최종 결과값
for i in range(N): # 각 관찰된 기록을 탐색
    pigeon_num=pigeon[i]
    pigeon_position=position[i]

    # CASE 1) 해당 비둘기가 처음 관찰됨
    if arr[pigeon_num]==-1:
        arr[pigeon_num]=pigeon_position
    # CASE 2) 해당 비둘기가 재관찰됨/ 위치 바뀜
    elif arr[pigeon_num]!=pigeon_position:
        cnt+=1
        arr[pigeon_num]=pigeon_position

print(cnt)
