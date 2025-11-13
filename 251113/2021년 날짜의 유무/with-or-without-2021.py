M, D = map(int, input().split())

# Please write your code here.
a=[1,3,5,7,8,10,12]
b=[4,6,9,11]

if M==2 and 1<=D<=28:
    print("Yes")
elif (M in a) and 1<=D<=31:
    print("Yes")
elif (M in b) and 1<=D<=30:
    print("Yes")
else:
    print("No")