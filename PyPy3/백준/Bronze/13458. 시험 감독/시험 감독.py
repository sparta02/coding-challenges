n = int(input())
arr= list(map(int, input().split()))

a, b = map(int, input().split())

result=0

for num in arr:
    result+=1
    num-=a
    if num>0:
        result+=(num+b-1)//b
print(result)