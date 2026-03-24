n=int(input())

result=[2,3,5,7]

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def cycle():
    global result
    new_list=[]
    for num in result:
        for i in range(1, 10):
            next=num*10+i
            if is_prime(next):
                new_list.append(next)
    result=new_list

if n!=1:
    for _ in range(n-1):
        cycle()

for num in result:
    print(num)