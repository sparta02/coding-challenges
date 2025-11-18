abilities = list(map(int, input().split()))

# Please write your code here.

def check(a,b,c):
    num1=abilities[a]+abilities[b]+abilities[c]
    num2=sum(abilities)-num1
    return abs(num1-num2)

min_num=99999999999999999999999999
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_num=min(min_num, check(i,j,k))

print(min_num)
