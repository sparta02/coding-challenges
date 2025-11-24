nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
check=0
for i in range(1, 40):
    for j in range(i, 40):
        for k in range(j, 40):
            for l in range(k, 40):
                temp_arr=[]
                temp_arr.append(i)
                temp_arr.append(j)
                temp_arr.append(k)
                temp_arr.append(l)
                temp_arr.append(i+j)
                temp_arr.append(i+k)
                temp_arr.append(i+l)
                temp_arr.append(j+k)
                temp_arr.append(j+l)
                temp_arr.append(k+l)
                temp_arr.append(i+j+k)
                temp_arr.append(i+j+l)
                temp_arr.append(i+k+l)
                temp_arr.append(j+k+l)
                temp_arr.append(i+j+k+l)
                temp_arr.sort()
                #print(temp_arr, nums)
                if nums==temp_arr:
                    print(i,j,k,l)
                    check=1
                    break
            if check:
                break
        if check:
                break
    if check:
                break
        