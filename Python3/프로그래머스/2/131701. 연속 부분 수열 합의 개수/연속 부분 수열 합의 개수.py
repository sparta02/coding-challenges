def solution(elements):
    answer = 0
    n=len(elements)
    elements*=2
    sum_list=[0]
    temp=0
    for num in elements:
        temp+=num
        sum_list.append(temp)
    # print(sum_list)
    
    temp_set=set()
    for i in range(1,n+1):
        for j in range(n):
            # print(j, i+j, sum_list[i+j]-sum_list[j])
            temp_set.add(sum_list[i+j]-sum_list[j])
    return len(temp_set)
