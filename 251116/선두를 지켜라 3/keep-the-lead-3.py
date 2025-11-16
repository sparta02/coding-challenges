n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a_idx=0
b_idx=0
a=[]
b=[]

for i in range(n):
    for j in range(t[i]):
        a_idx+=v[i]
        a.append(a_idx)

for i in range(m):
    for j in range(t2[i]):
        b_idx+=v2[i]
        b.append(b_idx)


cnt=0
point=999
for i in range(len(a)):
    temp=point
    if a[i]>b[i]:
        point=1
    elif a[i]<b[i]:
        point=-1
    elif a[i]==b[i]:
        point=0
    if point!=999 and temp!=point:
        cnt+=1


print(cnt)