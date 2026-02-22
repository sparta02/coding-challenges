n=int(input())
consults=[]

for i in range(1, n+1):
    t, p = map(int, input().split())
    if i+t>n+1:
        continue
    consults.append((i, i+t-1, p))

# print(consults)
result=0

def calc():
    time_table= [0]*(n+1)
    temp_value=0
    for i in range(len(consults)):
        t_or_f=select[i]
        if t_or_f==1:
            s, e, v= consults[i]
            for j in range(s, e+1):
                if time_table[j]==1:
                    return -1
                time_table[j]=1
            temp_value+=v
    return temp_value

select=[]

def choose(num):
    global result
    if num==len(consults):
        result=max(result,calc())
        return

    select.append(0)
    choose(num+1)
    select.pop()
    select.append(1)
    choose(num+1)
    select.pop()

choose(0)
print(result)