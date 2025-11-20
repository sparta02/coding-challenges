A, B, C = map(int, input().split())

# Please write your code here.

A, B= max(A,B), min(A,B)

A길이=C//A
B길이=C//B

result=0
for i in range(A길이+2):
    for j in range(B길이+2):
        temp=i*A+j*B
        차이=abs(temp-C)
        #print(i, j, result, temp, 차이)
        if temp<=C and (C-result)>차이:
            result=max(result, temp)

print(result)