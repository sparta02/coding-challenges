n, m = map(int, input().split())

arr=[0]+list(map(int, input().split()))

commands=[]

for _ in range(m):
    a, b= map(int, input().split())
    commands.append([a, b])

presum=[0]*(n+1)
for i in range(1, n+1):
    presum[i]= presum[i-1]+arr[i]

# print(presum)

for a, b in commands:
    print(presum[b]-presum[a-1])