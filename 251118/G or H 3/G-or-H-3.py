n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 1 2 3 4 5 6/ len(x)=6, k=2
result=0
for i in range(1, max(x)-k+1):
    temp=0
    #print(f"i: {i}")
    for j in range(len(x)):
        if i<=x[j]<=i+k:
            #print(x[j])
            if c[j]=="G":
                temp+=1
            elif c[j]=="H":
                temp+=2
    result=max(result, temp)

print(result)
