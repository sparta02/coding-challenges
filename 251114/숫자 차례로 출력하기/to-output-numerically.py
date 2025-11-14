n = int(input())

# Please write your code here.
stand=n

def a1(n):
    if n==0:
        return
    
    print(stand-n+1, end=" ")
    a1(n-1)

def a2(n):
    if n==0:
        return
    
    print(n, end=" ")
    a1(n-1)

a1(n)
print()
a2(n)