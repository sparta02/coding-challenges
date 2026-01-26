answer = 0
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1 ]

def print_storage(storage):
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            print(storage[i][j], end=" ")
        print()
    print()
    
    
def dfs(x,y, storage):
    visited = [[False]*len(storage[0]) for _ in range(len(storage))]
    stack=[]
    stack.append((x,y))
    while(stack):
        curr_x, curr_y=stack.pop()
        visited[curr_x][curr_y]=True
        #print(f"현재위치:{curr_x}, {curr_y}")
        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]
            if not (0<=temp_x<len(storage) and 0<=temp_y<len(storage[0])):
                #print("탈출")
                return True
            if storage[temp_x][temp_y]==0 and visited[temp_x][temp_y]==False:
                stack.append((temp_x,temp_y))
                visited[temp_x][temp_y]=True
    #print("아 이거 안된다")
    return False
              
    
def remove1(storage, alpha):
    global answer
    #print(f"{alpha} 조건부 삭제")
    
    # 임시 배열 생성
    temp_storage=[ x[:] for x in storage]
    
    for x in range(len(storage)):
        for y in range(len(storage[0])):
            # 특정 칸에서 밖으로 나갈 수 있는지 확인
            if storage[x][y]==alpha and dfs(x,y, storage):
                answer+=1
                temp_storage[x][y]=0
    return temp_storage

    
def remove2(storage, alpha):
    global answer
    #print(f"{alpha} 모두 삭제")
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j]==alpha:
                answer+=1
                storage[i][j]=0
    return storage
    

    
def solution(storage, requests):
    storage= [ list(x) for x in storage]
    
    global answer
    for req in requests:
        if len(req)==1:
            storage=remove1(storage, req)
        else:
            storage=remove2(storage, req[0])
        #print(answer)
        #print_storage(storage)
    
            
    return len(storage)*len(storage[0])-answer