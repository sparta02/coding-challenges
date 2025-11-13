n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n1-n2+1<1:
    print("No")
else: 
    arr=[[a[j]for j in range(i, i+n2)] for i in range(n1-n2+1)]
    for i in range(n1-n2+1):
        if arr[i]==b:
            print("Yes")
            break
    else:
        print("No")
