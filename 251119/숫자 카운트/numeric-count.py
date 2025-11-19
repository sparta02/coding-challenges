n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.

def check(B_num, a):

    count_1=0
    count_2=0
    B_num=str(B_num)
    a=str(a)

    if B_num[0]==a[0]:
        count_1+=1
    if B_num[1]==a[1]:
        count_1+=1
    if B_num[2]==a[2]:
        count_1+=1
    if a[0]==B_num[1]:
        count_2+=1
    if a[0]==B_num[2]:
        count_2+=1
    if a[1]==B_num[0]:
        count_2+=1
    if a[1]==B_num[2]:
        count_2+=1
    if a[2]==B_num[0]:
        count_2+=1
    if a[2]==B_num[1]:
        count_2+=1
    
    return (count_1, count_2)

cnt=0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or k==i:
                continue
            temp=True
            for l in range(n):
                if (b[l], c[l]) != check (i*100+j*10+k, a[l]):
                    temp=False
                    break
            if temp:
                cnt+=1

print(cnt)
