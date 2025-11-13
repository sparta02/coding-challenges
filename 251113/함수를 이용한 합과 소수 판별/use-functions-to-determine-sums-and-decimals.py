a, b = map(int, input().split())

# Please write your code here.
def check(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if sum(list(map(int, str(n))))%2!=0:
        return False
    return True

cnt=0
for i in range(a, b+1):
    if check(i):
        cnt+=1

print(cnt)