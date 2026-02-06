
def check(num_list):
    for i in range(len(num_list)//2):
        if num_list[i] != num_list[len(num_list)-i-1]:
            return 0
    return 1

result=0
while(1):
    num=list(input())
    if num ==['0']:
        break

    if check(num):
        print('yes')
    else:
        print('no')

