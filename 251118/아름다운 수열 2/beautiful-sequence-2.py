N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
print(f"B: {B}")
# Please write your code here.
cnt=0
for i in range(N-M+1):
    temp=A[i:i+M]
    #print(temp)
    temp.sort()
    #print(temp)
    if temp==B:
        cnt+=1

print(cnt)