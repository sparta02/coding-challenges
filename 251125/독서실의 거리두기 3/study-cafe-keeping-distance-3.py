N = int(input())
seat = input()
seats=[int(x) for x in seat]

# Please write your code here.
left=0

standard=0
최대값=0
최대_left=0
최대_right=0
for i in range(1, N):
    if seats[i]==1:
        #print(i, left)
        차이=i-left
        if 차이>최대값:
            최대값=차이
            최대_left=left
            최대_right=i
        left=i
       
#print(최대값)
#print(최대_left, 최대_right)
seats[int((최대_left+최대_right)/2)]=1

left=0

standard=0
최소값=9999999999
최대_left=0
최대_right=0
for i in range(1, N):
    if seats[i]==1:
        #print(i, left)
        차이=i-left
        최소값=min(최소값, 차이)
       
print(최소값)