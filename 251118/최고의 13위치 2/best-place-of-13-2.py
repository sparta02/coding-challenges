N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# Please write your code here.

max_num=0
for x1 in range(N):
    for y1 in range(N-2):
        for x2 in range(N):
            for y2 in range(N-2):
                #print(x1,y1,x2,y2)

                if abs(y1-y2)<=2 and x1==x2:
                    continue
                if arr[x1][y1]+arr[x1][y1+1]+arr[x1][y1+2]+arr[x2][y2]+arr[x2][y2+1]+arr[x2][y2+2]>max_num:
                    max_num=arr[x1][y1]+arr[x1][y1+1]+arr[x1][y1+2]+arr[x2][y2]+arr[x2][y2+1]+arr[x2][y2+2]
                #print(max_num)

print(max_num)

    