n = int(input())
l_arr = []
r_arr = []
for _ in range(n):
    left, right = map(int, input().split())
    l_arr.append(left)
    r_arr.append(right)

# Please write your code here.

cnt=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp_arr=[0]*(max(r_arr)+1)
            for l in range(n):
                if i==l or j==l or k==l:
                    continue
                for index in range(l_arr[l], r_arr[l]+1):
                    temp_arr[index]+=1
            flag=0
            for index in range(len(temp_arr)):
                if temp_arr[index]>=2:
                    flag=1
            if flag==0:
                cnt+=1

print(cnt)

                