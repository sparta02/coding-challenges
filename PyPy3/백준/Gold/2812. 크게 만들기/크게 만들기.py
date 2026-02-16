n, k = map(int, input().split())
arr= list(map(int, input()))

stack=[]

# 최대 k번까지 pop
# 무조건 앞자리가 커야함


# 앞자리가 더 작다면, pop
def arrange(i):
    global k
    next_num=arr[i]
    while(len(stack)!=0 and stack[-1]<next_num and k>0):
        stack.pop()
        k-=1
    stack.append(next_num)



for i in range(n):
    # print(i)
    if len(stack)==0:
        stack.append(arr[i])

    elif k>0:
        arrange(i)
    else:
        stack.append(arr[i])
    # print(stack)
    # print(f"k:{k}")
    # print()

while(k):
    stack.pop()
    k-=1

print("".join(list(map(str, stack))))