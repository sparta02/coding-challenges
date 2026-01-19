n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
dp1=[1]*n

for i in range(1, n):
    for j in range(i):
        if sequence[j]<sequence[i] and dp1[j]+1>dp1[i]:
            dp1[i]=dp1[j]+1

#print(dp1)

sequence=sequence[::-1]
#print(sequence)

dp2=[1]*n

for i in range(1, n):
    for j in range(i):
        if sequence[j]<sequence[i] and dp2[j]+1>dp2[i]:
            dp2[i]=dp2[j]+1
dp2=dp2[::-1]
#print(dp2)

dp3=[1]*n

for i in range(n):
    dp3[i]=dp1[i]+dp2[i]-1
#print(dp3)

print(max(max(dp1), max(dp2), max(dp3)))

