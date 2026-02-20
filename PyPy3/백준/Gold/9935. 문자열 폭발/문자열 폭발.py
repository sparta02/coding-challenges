text=input()
bomb=input()

stack=[]

def check():
    if len(stack)>=len(bomb):
        flag=1
        for a, b in zip(stack[-len(bomb):], bomb):
            if a!=b:
                flag=0
        if flag:
            for _ in range(len(bomb)):
                stack.pop()
    


for i in text:
    stack.append(i)
    # print(stack)
    check()

if len(stack):
    print("".join(stack))
else:
    print('FRULA')