import sys
sys.setrecursionlimit(10**4)

def make_star(n):
    if n==1:
        return '*'
    
    block=make_star(n//3)

    L=[]

    for line in block:
        L.append(line*3)
    for line in block:
        L.append(line+' '*(n//3) + line)
    for line in block:
        L.append(line*3)
    return L

n= int(input())
result=make_star(n)
for line in result:
    print(line)