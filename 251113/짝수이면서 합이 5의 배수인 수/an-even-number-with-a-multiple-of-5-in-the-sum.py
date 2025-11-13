n = int(input())

# Please write your code here.

def a(n):
    
    if n%2==0 and sum(list(map(int, str(n))))%5==0:
        result="Yes"
    else:
        result="No"
    return result
print(a(n))