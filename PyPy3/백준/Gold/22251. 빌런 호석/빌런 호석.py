n,k,p,original_x=map(int, input().split())
x=list(map(int, str(original_x)))

temp_list=[0]*(k-len(x))
x=temp_list+x
# print(x)

# 1~n 숫자, k자리
# x층에서 최대 p개를 반전시켜서 만들 수 있는 숫자 개수

bit_list=[0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,0b1011011,0b1011111,0b1110000,0b1111111,0b1111011]

result=0
select=[]

def check_num():
    return_num=0
    for i in select:
        return_num*=10
        return_num+=i
    # print(select)
    # print(return_num)
    return return_num

def choose(num):
    global result
    if num==k:
        # k자리수가 되었을 때
        # p번 이내로 반전시켜서 만들 수 있는지 확인 
        temp=0
        for i in range(k):
            temp+=bin(bit_list[select[i]]^bit_list[x[i]]).count('1')
        # p번 이내로 반전시켜서 만들 수 있고
        if temp<=p :
            #처음 주어진 n보다 작다면
            if check_num()<=n:
                # print(f"{select} is okay")
                
                result+=1
            # 만약 0000이면 제외
            if check_num()==0:
                result-=1
            # 만약 자기자신이면 제외
            if check_num()==original_x:
                result-=1
        return
    
    for i in range(10):
        select.append(i)
        choose(num+1)
        select.pop()






choose(0)
print(result)