T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
arr_S=[]
arr_N=[]
for i in range(T):
    if c[i]=="S":
        arr_S.append(x[i])
    if c[i]=="N":
        arr_N.append(x[i])
cnt=0
for i in range(a, b+1):
    min_S=99999999999999999
    min_N=99999999999999999
    for j in arr_S:
        min_S=min(min_S, abs(i-j))
    for j in arr_N:
        min_N=min(min_N, abs(i-j))
    if min_S<=min_N:
        cnt+=1
print(cnt)