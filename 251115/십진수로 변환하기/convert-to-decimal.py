binary = input()

# Please write your code here.
sum=0
for i in range(len(binary)):
    sum = sum*2 + int(binary[i])

print(sum)