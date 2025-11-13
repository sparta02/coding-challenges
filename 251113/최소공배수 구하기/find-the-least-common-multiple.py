n, m = map(int, input().split())

# Please write your code here.
a=1
while(True):
    if (n*a)%m==0:
        print(n*a)
        break
    else:
        a+=1