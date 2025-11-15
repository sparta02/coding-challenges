m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]

cnt=0

while True:
    if m1==m2 and d1==d2:
        break

    cnt+=1
    d1+=1

    if d1 > arr[m1]:
        m1+=1
        d1=1

print(cnt+1)
    