n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.

dp=[0]*(max(x2)+1)

# 선이 나올 수 있는 모든 점에 대해
for i in range(2, max(x2)+1):
    #print(f"{i}점 확인")
    # i점을 끝점으로 가지는 선분들을 추가
    temp_lines=[]
    for j in range(n):
        if x2[j]==i:
            temp_lines.append(j)
    # print(f"테스트할 점들:{temp_lines}")
    # print(temp_lines)

    # 만약 아무 선도 추가하지 않았을 경우
    # i-1의 값을 가져옴
    temp_result=dp[i-1]
    
    for j in temp_lines:
        temp_x1=x1[j]
        temp_x2=x2[j]
        
        temp_result=max(temp_result, dp[temp_x1-1]+1)
    dp[i]=temp_result

    # print(dp)
#print(dp)
print(max(dp))