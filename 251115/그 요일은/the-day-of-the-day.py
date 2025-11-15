m1, d1, m2, d2 = map(int, input().split())
A = input()


arr=[0,31,29,31,30,31,30,31,31,30,31,30,31]

def calc(m, d):
    cnt=0
    a=1
    b=1
    while True:
        if a==m and b==d:
            return cnt
        
        cnt+=1
        b+=1

        if arr[a]<b:
            a+=1
            b=1


day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

idx = (calc(m2, d2)-calc(m1, d1))//7

print(idx+1)