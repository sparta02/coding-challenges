binary = list(map(int, input()))

# Please write your code here.
result=0
j=0
for i in binary[::-1]:
    result+=i*(2**j)
    j+=1

print(result)