n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t2 = []
d2 = []
for _ in range(m):
    time, direction = input().split()
    t2.append(int(time))
    d2.append(direction)

# Please write your code here.


a=[]
a_idx=0
b=[]
b_idx=0
for i in range(n):
    if d[i]=='R':
        for j in range(t[i]):
            a_idx+=1
            a.append(a_idx)
    else:
        for j in range(t[i]):
            a_idx-=1
            a.append(a_idx)

for i in range(m):
    if d2[i]=='R':
        for j in range(t2[i]):
            b_idx+=1
            b.append(b_idx)
    else:
        for j in range(t2[i]):
            b_idx-=1
            b.append(b_idx)


cnt=0

for i in range(max(len(a),len(b))):
    if i==0:
        continue
    if (a[i-1]!= b[i-1] and a[i]== b[i]):
        cnt+=1

print(cnt)


    