import sys
str = input()

# Please write your code here.

list=[]

for i in str:
    if i=='(':
        list.append('(')
    else:
        if len(list)<=0:
            print("No")
            sys.exit()
        else:
            list.pop()
if len(list)==0:
    print("Yes")
else:
    print("No")