n= int(input())
prime_num=[]

def is_prime(num):
    if num==2:
        return True
    for i in range(2, int(num**0.5)+2):
        if num%i==0:
            return False
    return True

for i in range(2, n+1):
    if is_prime(i):
        prime_num.append(i)
# print(prime_num)
result=0
i, j=0,0
if len(prime_num):
    sum=prime_num[0]
    while i<len(prime_num):
        while sum<n and j<len(prime_num)-1:
            j+=1
            sum+=prime_num[j]
        
        # print(i, j)
        # print(sum)
        if sum==n:
            # print("ok")
            result+=1
        sum-=prime_num[i]
        i+=1

print(result)