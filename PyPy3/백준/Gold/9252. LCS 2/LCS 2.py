A=list(input())
B=list(input())
a=len(A)
b=len(B)

# dp[i][j]
dp = [ [0]*b for i in range(a)]

def print_dp():
    print("", end="  ")
    print(*B)
    for i in range(a):
        print(A[i], end=" ")
        for j in range(b):
            print(dp[i][j], end=" " )
        print()
    print()

dp[0][0]=1 if A[0]==B[0] else 0

for i in range(1, a):
    if B[0]==A[i]:
        dp[i][0]=1
    else:
        dp[i][0]=dp[i-1][0]

for j in range(1, b):
    if B[j]==A[0]:
        dp[0][j]=1
    else:
        dp[0][j]=dp[0][j-1]

for i in range(1, a):
    for j in range(1, b):
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

new_dp=[[0]*(b+1)]
for i in range(a):
    new_dp.append([0]+dp[i])

A=[0]+A
B=[0]+B
def print_new_dp():
    print("", end="  ")
    print(*B)
    for i in range(a+1):
        print(A[i], end=" ")
        for j in range(b+1):
            print(new_dp[i][j], end=" " )
        print()
    print()

# print_dp()
# print_new_dp()


# print(a, b)
result=[]
print(dp[-1][-1])
if new_dp[-1][-1]:
    curr_a, curr_b=a, b
    while new_dp[curr_a][curr_b]!=0:
        if curr_a>0 and new_dp[curr_a-1][curr_b]==new_dp[curr_a][curr_b]:
            curr_a-=1
        elif curr_b>0 and new_dp[curr_a][curr_b-1]==new_dp[curr_a][curr_b]:
            curr_b-=1
        else:

            result.append(A[curr_a])
            curr_a-=1
            curr_b-=1
result=result[::-1]
print("".join(result))
        
