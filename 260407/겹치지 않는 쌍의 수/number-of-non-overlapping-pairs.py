n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

groups=[]
for temp in arr:
    temp=temp[1:]
    S=0
    for i in temp:
        S|=(1<<i)
    groups.append(S)

result=0
for i in range(n):
    for j in range(i+1, n):
        if not(groups[i]&groups[j]):
            result+=1

print(result)