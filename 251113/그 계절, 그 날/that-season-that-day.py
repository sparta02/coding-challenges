Y, M, D = map(int, input().split())

# Please write your code here.
a=[1,3,5,7,8,10,12]
b=[2,4,6,9,11]

def check_year(Y):
    if (Y%4==0 and Y%100!=0) or Y%400==0:
        return True
    else:
        return False

def check_day(Y, M, D):
    if M in a:
        if 1<=D<=31:
            return True
    elif M in b:
        if 1<=D<=30:
            return True
    elif M==2:
        if check_year(Y) and 1<=D<=29:
            return True
        elif 1<=D<=28:
            return True
    return False

if check_day(Y, M, D) == False:
    print(-1)
elif 3<=M<=5:
    print("Spring")
elif 6<=M<=8:
    print("Summer")
elif 9<=M<=11:
    print("Fall")
else:
    print("Winter")