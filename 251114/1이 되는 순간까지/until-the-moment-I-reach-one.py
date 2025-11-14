N = int(input())

# Please write your code here.
cnt=0

def calc(n):
    if n==1:
        return

    if n%2==0:
        n=int(n/2)
    else:
        n=int(n/3)
    global cnt
    cnt+=1
    calc(n)

calc(N)
print(cnt)