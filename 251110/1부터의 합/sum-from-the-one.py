a= int(input())
sum=0


for i in range (1, a+1):
    if(sum>=a):
        print(i-1)
        break;
    sum+=i
