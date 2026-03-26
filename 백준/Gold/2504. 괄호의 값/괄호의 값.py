import sys
input = sys.stdin.readline

arr=input()
stack=[]

for i in arr:
    if i=='(':
        stack.append(i)
    elif i=='[':
        stack.append(i)
    elif i==')':
        temp=2
        next=''
        while next!='(':
            if len(stack)==0:
                print(0)
                sys.exit()
            next=stack.pop()
            if next in ('[', ')', ']'):
                print(0)
                sys.exit()
            if next != '(':
                temp*=next
        stack.append(temp)
    elif i==']':
        temp=3
        next=''
        while next!='[':
            if len(stack)==0:
                print(0)
                sys.exit()
            next=stack.pop()
            if next in ('(', ')', ']'):
                print(0)
                sys.exit()
            if next != '[':
                temp*=next
        stack.append(temp)
    if len(stack)>=2:
        if str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
            a= stack.pop()
            b= stack.pop()
            stack.append(a+b)
    # print(stack)

if len(stack)!=1:
    print(0)
    sys.exit()
result=stack.pop()

if str(result).isdigit() != True:
    print(0)
    sys.exit()

print(result)