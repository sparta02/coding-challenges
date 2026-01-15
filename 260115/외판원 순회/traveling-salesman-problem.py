n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

visited=[False]*n
visited[0]=True
# Please write your code here.
temp_list=[]
result_cost=999999999999999


def print_cost():
    global result_cost
    result=0
    for i in range(n):
        result+=cost[temp_list[i][0]][temp_list[i][1]]
    #print(result)
    # if result==50:
    #     print(temp_list)
    result_cost=min(result_cost, result)


def move(curr_num):

    # n-1개를 방문하면 종료
    if curr_num == n-1:
        # 가장 마지막 node에서 0으로 돌아가는 경로 추가
        temp_list.append([temp_list[-1][1], 0])

        #print(temp_list)

        # 마지막 node에서 0으로 돌아가는게 불가능하면 스킵
        if cost[temp_list[-2][1]][0]==0:
            temp_list.pop()
            return
        
        #가능하다면 cost 계산
        print_cost()
        temp_list.pop()
        return

    # 0~n-1 노드를 모두 돌며 확인
    for i in range(n):
        #print(visited)
        #print(temp_list)
        
        # 이미 i번째 노드를 방문했다면 skip
        if visited[i] == True:
            continue

        # cost[이전노드][i]가 0이라면 스킵
        if (cost[0][i]==0 if len(temp_list)==0 else cost[temp_list[-1][1]][i]==0):
            continue
        
        # 현재 i노드 방문처리
        visited[i]=True
        temp_list.append([0 if len(temp_list)==0 else temp_list[-1][1], i])

        move(curr_num+1)

        visited[i]=False
        temp_list.pop()



move(0)

print(result_cost)