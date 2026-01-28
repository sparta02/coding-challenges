n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.

maps_A={}

for a in A:
    maps_A[a]=maps_A.get(a, 0)+1

maps_A_B={}
for b in B:
    for a_key, a_value in maps_A.items():
        maps_A_B[b+a_key]=maps_A_B.get(b+a_key, 0)+maps_A[a_key]

# print(maps_A_B)

maps_C={}

for c in C:
    maps_C[c]=maps_C.get(c, 0)+1

maps_C_D={}
for d in D:
    for c_key, c_value in maps_C.items():
        maps_C_D[d+c_key]=maps_C_D.get(d+c_key, 0)+maps_C[c_key]

# print(maps_C_D)


result=0
for i, j in maps_A_B.items():
    result+=maps_C_D.get(-i, 0)*j

print(result)