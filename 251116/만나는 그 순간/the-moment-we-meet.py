n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

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


result=-1
cnt=0

for i in range(max(len(a),len(b))):
    if a[i]==b[i]:
        result=i+1
        break

print(result)


    