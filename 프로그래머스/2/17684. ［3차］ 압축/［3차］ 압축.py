def find_longgest_string(msg, dict):
    result=-1

    for i in range(len(msg)):
        temp_string=msg[:i+1]
        temp_string="".join(temp_string)
        
        if temp_string in dict:
            result=i
        else:
            break
    return result
    

def solution(msg):
    msg=list(msg)
    answer = []
    
    
    dict={}
    for i in range(1, 27):
        dict[chr(64+i)]=i
    #print(dict)
    dict_index=27
    
    
    while(len(msg)):
        # i번째 문자를 기준으로
        # 해당 문자를 포함하여 이미 사전에 등록되어 있는
        # 가장 긴 문자열을 찾기
        # apple 이라면 a, ap, app, appl, apple
        index=find_longgest_string(msg, dict)
        #print(index)
        answer.append(dict["".join(msg[:index+1])])
        dict["".join(msg[:index+2])]=dict_index
        dict_index+=1
        
        for _ in range(index+1):
            msg.pop(0)
    #print(dict)

    return answer