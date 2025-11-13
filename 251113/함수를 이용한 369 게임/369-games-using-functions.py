a, b = map(int, input().split())

# Please write your code here.
def check1(n):
    arr=str(n)

    if '3' in arr:
        return True
    elif '6' in arr:
        return True
    elif '9' in arr:
        return True
    else:
        return False

def check2(n):
    return n%3==0

cnt=0
for i in range(a, b+1):

    if check1(i) or check2(i):
        cnt+=1

print(cnt)