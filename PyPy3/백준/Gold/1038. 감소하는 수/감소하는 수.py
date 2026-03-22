import sys
n= int(input())

num_list=[]
cnt=-1

# if n>1021:
#     print(-1)
#     sys.exit()

def choose(num, curr):
    global cnt
    if num==curr:
        # print(num_list)
        cnt+=1
        if cnt==n:
            print("".join(map(str, num_list)))
            sys.exit()
        return

    flag= 10 if len(num_list)==0 else num_list[-1]
    for i in range(flag):
        num_list.append(i)
        choose(num, curr+1)
        num_list.pop()


# 1~9자리수
for i in range(1, 13):
    # n번째 자리수는 n-1 이상이여야 함
    choose(i,0)

print(-1)