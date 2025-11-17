a = input()

# Please write your code here.
a=a.replace("0","1",1)

sum=0
for i in range(len(a)):
    sum= sum*2 +int(a[i])
print(sum)