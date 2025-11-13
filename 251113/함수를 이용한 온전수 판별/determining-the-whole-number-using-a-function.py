a, b = map(int, input().split())

# Please write your code here.
def check(n):
    if a%2==0:
        return False
    elif a%10==5:
        return False
    elif a%3==0 and a%9!=0:
        return False
    else:
        return True

cnt=0
for i in range(a, b+1):
    if check(i):
        cnt+=1
print(cnt)