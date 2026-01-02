from collections import deque

n, k = map(int, input().split())

# Please write your code here.

dq = deque()

for i in range(1, n+1):
    dq.append(i)

# print("초기")
# print(dq)
# print("")


while(len(dq)):
    for _ in range(k-1):
        temp=dq.popleft()
        dq.append(temp)
        # print(dq)
    print(dq.popleft(), end=" ")
    # print(dq)
