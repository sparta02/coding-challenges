a = input()

# Please write your code here.
b=a.replace("0","1",1)
if a==b:
    b=a-1
sum=0
for i in range(len(b)):
    sum= sum*2 +int(b[i])
print(sum)