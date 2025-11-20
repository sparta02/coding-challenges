X, Y = map(int, input().split())

# Please write your code here.

def calc(a):
    sum=0
    while a>0:
        sum=sum+a%10
        a//=10
    return sum

max_num=0
for i in range(X, Y+1):
    #print(calc(i))
    max_num=max(max_num, calc(i))

print(max_num)