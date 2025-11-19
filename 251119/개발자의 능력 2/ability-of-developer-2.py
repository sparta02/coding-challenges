arr = list(map(int, input().split()))

# Please write your code here.
result=999999

for i in range(6):
    new_arr1=arr[:]
    a=new_arr1.pop(i)
    for j in range(5):
        new_arr2=new_arr1[:]
        b=new_arr2.pop(j)
        for k in range(4):
            new_arr3=new_arr2[:]
            c=new_arr3.pop(k)
            for l in range(3):
                new_arr4=new_arr3[:]
                d=new_arr4.pop(l)
                #print(a,b,c,d)
                A=a+b
                C=c+d
                E=sum(arr)-A-C
                차이=max(A,C,E)-min(A,C,E)
                result=min(result, 차이)


        

print(result)
    