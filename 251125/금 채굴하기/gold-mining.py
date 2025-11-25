n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

result=0
for x in range(n):
    for y in range(n):
        
        for k in range(n):
            gold=0
            
            #print(f"x:{x}, y:{y}, k:{k}")
            for i in range(n):
                for j in range(n):
                    if (abs(x-i)+abs(y-j))<=k:
                        gold+=grid[i][j]
                        #print(f"i:{i}, j:{j}")
            
            #print(f"금값:{gold*m}, 비용: {(k**2+(k+1)**2)}")
            이윤=gold*m-(k**2+(k+1)**2)
            
            if 이윤>=0:
                result=max(result, gold)

print(result)

