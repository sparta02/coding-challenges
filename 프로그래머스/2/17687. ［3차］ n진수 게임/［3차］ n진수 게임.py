def make_num_list(n):
    num_list=['0']
    # n진법
    for i in range(100000):
        curr_num=i
        temp_list=[]
        while(curr_num):
            한자리=curr_num%n
            if 10<=한자리<=15:
                temp_list.append(chr(한자리+55))
            else:
                temp_list.append(str(한자리))
            curr_num//=n
        num_list.extend(temp_list[::-1])
    return num_list
                

def solution(n, t, m, p):
    answer = ''
    num_list=make_num_list(n)
    #print(num_list)
    for i in range(t):
        #print(p-1+m*i)
        answer+=num_list[p-1+m*i]
    
    
    return answer
    