n=int(input())
arr=list(map(int, input().split()))
stack=[]

for i in range(n):
    curr=arr[i]
    if len(stack)==0:
        print(0, end=" ")
        stack.append(i)
    else:
        while stack:
            next=stack.pop()
            if arr[next]>=curr:
                print(next+1, end=" ")
                stack.append(next)
                stack.append(i)
                break
            else:
                if len(stack)==0:
                    print(0, end=" ")
                    stack.append(i)
                    break
                else:
                    continue
    # print(stack)
