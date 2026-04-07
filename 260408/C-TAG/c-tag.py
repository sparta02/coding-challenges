from itertools import combinations
n, m = map(int, input().split())

A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(n)]

comb =list(combinations(range(m), 3))
result=0
for a,b,c in comb:
    hash_A=set()
    for str in A:
        hash_A.add("".join(str[a]+str[b]+str[c]))
    
    for str in B:
        temp="".join(str[a]+str[b]+str[c])
        if temp in hash_A:
            break
    else:
        result+=1
print(result)