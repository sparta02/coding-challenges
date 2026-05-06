import sys
n = int(input())
if n==0:
    print(0)
    sys.exit()
# Please write your code here.

temp=[]

while n:
    temp.append(str(n%2))
    n//=2
temp=temp[::-1]
print("".join(temp))