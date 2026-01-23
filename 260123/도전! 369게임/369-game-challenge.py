n = input()

# Please write your code here.
result=0
for i in range(1, int(n)+1):
    if i%3==0 or str(3) in str(i) or str(6) in str(i) or str(9) in str(i):
        result+=1
print(result%(10**9+7))