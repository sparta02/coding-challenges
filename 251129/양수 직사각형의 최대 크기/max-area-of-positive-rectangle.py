n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result=-1


for x in range(1, n+1): # 세로 길이
    for y in range(1, m+1): # 가로 길이

        for i in range(0, n-x+1): # x축 검사 시작 위치
            for j in range(0, m-y+1): # x축 검사 시작 위치
            # x가 2, y가 2라면
            # i는 0~2까지, j는 0~3까지 돌면서 확인
                #print(f"x:{x}, y:{y}, i:{i}, j:{j}")
                check=1
                for x_check in range(i, i+x):
                    for y_check in range(j, j+y):
                        # 만약 음수가 발견되면 check를 0으로 설정
                        if grid[x_check][y_check]<=0:
                            check=0
                # 모든 요소가 양수라면
                if check:
                    result=max(result, x*y)

print(result)

                    