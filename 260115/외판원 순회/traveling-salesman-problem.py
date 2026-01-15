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

    result_cost=min(result_cost, result)

def move(curr_num):
    if curr_num == n-1:
        temp_list.append([temp_list[-1][1], 0])
        #print(temp_list)
        print_cost()
        temp_list.pop()
        return

    for i in range(n):
        # print(visited)
        # print(temp_list)
        if visited[i] == True or curr_num == i:
            continue
        
        visited[i]=True
        temp_list.append([curr_num, i])

        move(curr_num+1)

        visited[i]=False
        temp_list.pop()



move(0)

print(result_cost)