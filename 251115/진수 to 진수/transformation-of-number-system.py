a, b = map(int, input().split())
n = input()

# Please write your code here.


# Please write your code here.
sum=0
n=str(n)

for i in range(len(n)):
    sum=sum*a+int(n[i])


arr=[]

while True:
    if sum<b:
        arr.append(sum)
        break
    arr.append(sum%b)
    sum//=b

print("".join(map(str, arr[::-1])))