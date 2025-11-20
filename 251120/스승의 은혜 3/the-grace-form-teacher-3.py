N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
max_num=0
for i in range(N):
    temp_arr=[]
    for j in range(N):
        temp_arr.append(P[j]+S[j] if i!=j else int(P[j]/2)+S[j])
        sum=0
    for k in range(N):
        sum+=temp_arr[k]
        if sum<=B:
            max_num=max(max_num,k+1)
        else:
            break

print(max_num)


