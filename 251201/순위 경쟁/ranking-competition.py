n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.

count=0
A=0
B=0
C=0
순위표=['A', 'B', 'C']

def 순위결정():
    새_순위표=[]
    max_num = max(A, B, C)
    if A==max_num:
        새_순위표.append('A')
    if B==max_num:
        새_순위표.append('B')
    if C==max_num:
        새_순위표.append('C')
    return 새_순위표


for i in range(n):
    if c[i]=='A':
        A+=s[i]
    elif c[i]=='B':
        B+=s[i]
    else:
        C+=s[i]
    새로운_순위표=순위결정()
    if 순위표 != 새로운_순위표:
        count+=1
    순위표= 새로운_순위표

print(count)
