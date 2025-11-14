n = int(input())

# Please write your code here.
stand=n

def a1(n):
    if n==0:
        return
    
    print(stand-n+1, end=" ")
    a1(n-1)

def a2(k):
    if k==0:
        return
    
    print(k, end=" ")
    a2(k-1)

a1(n)
print()
a2(n)