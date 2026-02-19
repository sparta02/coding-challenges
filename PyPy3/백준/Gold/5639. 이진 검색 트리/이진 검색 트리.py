import sys

sys.setrecursionlimit(30000)
input = sys.stdin.readline

nodes = []

while True:
    line = input().strip()
    if not line:
        break
    nodes.append(int(line))

def post_order(start, end):
    # 데이터가 1개도 없는 범위라면 종료
    if start >= end:
        return

    root = nodes[start]
    
    # 분할 지점 초기값을 end로 설정 

    division = end 
    for i in range(start + 1, end):
        if nodes[i] > root:
            division = i
            break

    # 왼쪽 서브트리 범위: [start + 1, division)
    post_order(start + 1, division)
    
    # 오른쪽 서브트리 범위: [division, end)
    post_order(division, end)
    
    # 마지막에 루트 출력
    print(root)

post_order(0, len(nodes))