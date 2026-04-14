n = int(input())

# Please write your code here.
temp=n//8
나머지=n%8
result=temp*15
if 나머지==1:
    result+=1
elif 나머지==2:
    result+=2
elif 나머지==3:
    result+=4
elif 나머지==4:
    result+=7
elif 나머지==5:
    result+=8
elif 나머지==6:
    result+=11
elif 나머지==7:
    result+=13
else:
    result-=1

print(result)