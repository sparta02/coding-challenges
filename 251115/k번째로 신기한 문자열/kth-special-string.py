n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
check_list=[]

for i in str:
    if i.find(t) ==0:
        check_list.append(i)

check_list.sort()
print(check_list[k-1])


