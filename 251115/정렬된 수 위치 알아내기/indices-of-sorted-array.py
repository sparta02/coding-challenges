n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
arr=[((i+1), seq) for i, seq in enumerate(sequence)]

arr.sort(key=lambda x: (x[1], x[0]))


idx_arr=[]
for i in range(1, n+1):
    for j in range(n):
        if i==arr[j][0]:
            idx_arr.append(j+1)

for i in range(n):
    print(idx_arr[i], end=" ")