import sys

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
new_arr=arr[:]
new_arr=list(set(new_arr))
new_arr.sort()

if len(new_arr)<2:
    print(-1)
    sys.exit()


second_num =new_arr[1]
#print(second_num)
if arr.count(second_num)>=2:
    print(-1)
    sys.exit()

print(arr.index(second_num)+1)