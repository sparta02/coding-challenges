N = int(input())
seat = input()
seats=[int(x) for x in seat]

# Please write your code here.
arr=[]
left=0
for i in range(1, N):
    if seats[i]==1:
        
        차이=i-left
        arr.append(차이)
        left=i

arr.sort()
temp=arr[-1]
arr[-1]=int(arr[-1]/2)
arr.append(temp-arr[-1])
print(min(arr))
