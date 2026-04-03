n=int(input())
result=0

hano=[0]*21
hano[1]=1
hano[2]=3
for i in range(3, 21):
    hano[i]=hano[i-1]*2+1

dp=[0]*21
dp[1]=1
dp[2]=3
dp[3]=5
for i in range(4, 21):
    dp[i]=dp[i-2]+3+hano[i-2]
print(dp[n])
def hanoi(num, start, mid, end):
    global result
    if num==1:
        result+=1
        print(start, end)
        return
    
    hanoi(num-1, start, end, mid)
    result+=1
    print(start, end)
    hanoi(num-1, mid, start, end)


one='A'
two='B'
three='C'
while n>0:
    if n==1:
        result+=1
        print(one, 'D')
        break
    elif n==2:
        result+=3
        print(one, two)
        print(one, 'D')
        print(two, 'D')
        break
    
    hanoi(n-2, one, two, three)
    result+=3
    print(one, two)
    print(one, 'D')
    print(two, 'D')
    n-=2
    one, three= three, one
    
# print(result)