N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

def check_index(x):
    if 0<=x<N:
        return True
    return False

max_num=0
for i in range(N):
    temp=num[i]
    for k in range(1,K+1):
        if check_index(i-k) and num[i-k]==temp:
            max_num=max(max_num, temp)
        if check_index(i+k) and num[i+k]==temp:
            max_num=max(max_num, temp)

print(max_num)
    

