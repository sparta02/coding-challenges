nums = list(map(int, input().split()))

# Please write your code here.
check=0
for i in range(40):
    for j in range(i, 40):
        for k in range(j, 40):
            for l in range(k, 40):
                if i in nums and j in nums and k in nums and l in nums and i+j in nums and j+k in nums and k+l in nums and i+k in nums and j+l in nums and i+j+k in nums and i+j+l in nums and i+k+l in nums and i+j+k+l in nums:
                    print(i,j,k,l)
                    check=1
                    break
            if check:
                break
        if check:
                break
    if check:
                break
        