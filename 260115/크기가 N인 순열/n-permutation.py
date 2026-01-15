n = int(input())
visited=[False]*(n+1)
# Please write your code here.

temp_list=[]

def print_list():
    for i in range(n):
        print(temp_list[i], end=" ")
    print()

def plus(curr_num):
    global visited
    global temp_list
    if curr_num == n:
        print_list()
        return

    for i in range(1, n+1):
        # print(visited)
        # print(temp_list)
        if visited[i]==True:
            continue
        
        temp_list.append(i)
        visited[i]=True

        plus(curr_num+1)

        temp_list.pop()
        visited[i]=False

plus(0)