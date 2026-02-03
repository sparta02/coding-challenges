n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

meetings=sorted(meetings, key = lambda x:x[1])

#print(meetings)

meet_list=[]

meet_list.append(meetings[0])

for i in range(1, n):
    if meetings[i][0]>=meet_list[-1][1]:
        meet_list.append(meetings[i])
#print(meet_list)

print(len(meet_list))