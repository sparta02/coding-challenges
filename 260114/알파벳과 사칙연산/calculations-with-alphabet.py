expression = input()

# Please write your code here.

def calc(temp_exp):
    result=int(temp_exp[0])
    # print(result)
    for i in range(len(temp_exp)):
        if temp_exp[i]=="+":
            result+=int(temp_exp[i+1])
        elif temp_exp[i]=="-":
            result-=int(temp_exp[i+1])
        elif temp_exp[i]=="*":
            result*=int(temp_exp[i+1])
    # print(result)
    return result


alpha=[]
result_num=-9999999999
def replace_alpha(n):
    global result_num
    if n==6:
        temp_exp=expression[:]
        # print(alpha)
        for i in range(6):
            temp_exp=temp_exp.replace(chr(97+i), str(alpha[i]))
        #print(temp_exp)

        result_num=max(result_num, calc(temp_exp))
        return

    for j in range(1, 5):
        alpha.append(j)
        replace_alpha(n+1)
        alpha.pop()

replace_alpha(0)
print(result_num)