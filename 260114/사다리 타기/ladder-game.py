import sys
from itertools import combinations

n, m = map(int, input().split())
temp_edges = [tuple(map(int, input().split())) for _ in range(m)]

edges=[ [x[1], x[0]] for x in temp_edges]
행수=max([x[0] for x in edges])

# Please write your code here.
def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

def ladder_result(new_edges):
    # 1. 사다리 세팅
    # print(행수)
    ladder=[ [0]*(n+1) for _ in range(행수+1)]

    # print(f"들어온 가지들: {new_edges}")
    for i in range(len(new_edges)):
        x=new_edges[i][0]
        y=new_edges[i][1]

        ladder[x][y]=1

    #print_grid(ladder)

    # 2. 사다리 결과
    result_list=[]
    for i in range(1, n+1):
        # print(f"{i}의 결과")
        for j in range(행수+1):
            # print(j, i)
            # 오른쪽으로 이동
            if ladder[j][i]==1:
                i+=1
            # 왼쪽으로 이동
            elif ladder[j][i-1]==1:
                i-=1
        #print(i)
        #print()
        result_list.append(i)
    return result_list


def main():
    
    standard_result=ladder_result(edges)
    # print(standard_result)
    # print()

    for i in range(n+1):
        # print(f"가지수 {i}개 테스트")
        comb=list(combinations(range(m),i))
        # print(comb)
        
        # 각 경우의 수에 대해
        for com in comb:
            new_edges=[]
            for t in range(i):
                new_edges.append(edges[com[t]])
            # print(f"테스트할 가지들: {new_edges}")

            new_result=ladder_result(new_edges)
            # print(new_result)
            # print()

            if new_result == standard_result:
                print(i)
                sys.exit()


    

if __name__ =="__main__":
    main()