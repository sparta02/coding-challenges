def solution(topping):
    answer = 0
    
    first=[]
    first_set=set()

    for num in topping:
        first_set.add(num)
        first.append(len(first_set))
    
    second=[]
    second_set=set()

    for num in topping[::-1]:
        second_set.add(num)
        second.append(len(second_set))
    second=second[::-1]
    
    for i in range(len(topping)-1):
        if first[i]==second[i+1]:
            answer+=1
    
    return answer