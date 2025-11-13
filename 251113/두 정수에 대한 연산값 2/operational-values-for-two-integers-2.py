a, b = map(int, input().split())

# Please write your code here.

def modify(a,b):
    if a>b:
        return (a*2,b+10)
    else:
        return (a+10,b*2)

a,b=modify(a,b)
print(a, b)