from functools import cmp_to_key


n = int(input())
arr = [int(input()) for _ in range(n)]

def compare(x, y):
    if int(str(x)+str(y))>int(str(y)+str(x)):
        return -1
    
    if int(str(x)+str(y))<int(str(y)+str(x)):
        return 1
    
    return 0

# Please write your code here.
arr.sort(key=cmp_to_key(compare))
arr=[str(x) for x in arr]
print("".join(arr))