def split_file(name):
    name=list(name)
    head, number=[], []
    num_index=-1
    for i in range(len(name)):
        if not name[i].isdigit():
            head.append(name[i].lower())
        else:
            num_index=i
            break
            
    for i in range(num_index, len(name)):
        if name[i].isdigit():
            number.append(name[i])
        else:
            break
    #print(head, number)
    return "".join(head), int("".join(number))

def solution(files):
    # 정렬하기 위해 필요한 것
    # 1. HEAD 부분(대소문자 구분 X)
    # 2. NUMBER 부분 (앞에 0이 있다면 제거)
    # 3. 입력할 때 들어온 순서
    files_refine=[]
    
    for i in range(len(files)):
        head, number = split_file(files[i])
        files_refine.append((head, number, i))
    #print(files_refine)
    files_refine.sort()
    #print(files_refine)
    
    answer = []
    for _, _, i in files_refine:
        answer.append(files[i])
    
    return answer