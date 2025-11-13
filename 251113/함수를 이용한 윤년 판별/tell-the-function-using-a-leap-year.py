y = int(input())

# Please write your code here.

def chk(n):
    if n%4==0 and n%400!=0:
        return "true"
    elif n%100==0 :
        return "true"
    return "false"

print(chk(y))