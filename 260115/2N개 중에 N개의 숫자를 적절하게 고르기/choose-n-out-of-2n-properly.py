n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
result=9999999999999999
temp_list=[]

def choose(i):
    global result
    if i==2*n:
        #print(temp_list)
        group_a=sum(temp_list)
        group_b=sum(num)-sum(temp_list)
        result=min(result,abs(group_a-group_b))
        return

    # 현재 num[i]을 추가하는 경우
    temp_list.append(num[i])
    choose(i+1)
    temp_list.pop()

    # 현재 num[i]를 스킵
    choose(i+1)


choose(0)

print(result)