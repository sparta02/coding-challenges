N, B = map(int, input().split())

# Please write your code here.

arr=[]

while True:
    if N<B:
        arr.append(N)
        break
    arr.append(N%B)
    N//=B
arr="".join(map(str, arr[::-1]))
print(arr)