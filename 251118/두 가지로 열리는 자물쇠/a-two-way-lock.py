N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

arr1=[a1,a1+1,a1+2,a1-1,a1-2]
arr2=[b1,b1+1,b1+2,b1-1,b1-2]
arr3=[c1,c1+1,c1+2,c1-1,c1-2]
arr4=[a2,a2+1,a2+2,a2-1,a2-2]
arr5=[b2,b2+1,b2+2,b2-1,b2-2]
arr6=[c2,c2+1,c2+2,c2-1,c2-2]

for i in range(5):
    if arr1[i]>N:
        arr1[i]=arr1[i]%N+1
    if arr2[i]>N:
        arr2[i]=arr2[i]%N+1
    if arr3[i]>N:
        arr3[i]=arr3[i]%N+1
    if arr1[i]<1:
        arr1[i]=arr1[i]+N
    if arr2[i]<1:
        arr2[i]=arr2[i]+N
    if arr3[i]<1:
        arr3[i]=arr3[i]+N

    if arr4[i]>N:
        arr4[i]=arr4[i]%N+1
    if arr5[i]>N:
        arr5[i]=arr5[i]%N+1
    if arr6[i]>N:
        arr6[i]=arr6[i]%N+1
    if arr4[i]<1:
        arr4[i]=arr4[i]+N
    if arr5[i]<1:
        arr5[i]=arr5[i]+N
    if arr6[i]<1:
        arr6[i]=arr6[i]+N



x=0
y=0
z=0

for i in range(5):
    if arr4[i] in arr1:
        x+=1
    if arr5[i] in arr2:
        y+=1
    if arr6[i] in arr3:
        z+=1
    
print(250-x*y*z)



