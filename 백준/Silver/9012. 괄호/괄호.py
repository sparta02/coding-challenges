from collections import deque
n= int(input())

for _ in range(n):
    arr=input()
    queue =deque()

    for st in arr:
        # (이 들어온 경우
        if st=='(':
            queue.append('(')
        else:
            if len(queue)==0:
                print("NO")
                break
            else:
                queue.pop()
        # print(queue)
    else:
        if len(queue)==0:
            print("YES")
        else:
            print("NO")
