def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key =lambda x:(x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        temp=i+1
        mod_sum=0
        for num in data[i]:
            mod_sum+=(num%temp)
        answer=answer^mod_sum

    return answer