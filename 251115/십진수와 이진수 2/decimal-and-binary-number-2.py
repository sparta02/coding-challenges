N = input()

# Please write your code here.
sum=0

for i in range(len(N)):
    sum=sum*2+int(N[i])

sum*=17

arr=[]

while True:
    if sum<2:
        arr.append(sum)
        break
    arr.append(sum%2)
    sum//=2

print("".join(map(str, arr[::-1])))