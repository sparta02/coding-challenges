n, s = map(int, input().split())
cars=list(map(int, input().split()))
oils=list(map(int, input().split()))


L=s-1
R=s-1
left_reach=cars[L]-oils[L]
right_reach=cars[L]+oils[L]
# print(left_reach,right_reach)

change=True
while change:
    change=False
    
    if L>0 and left_reach<=cars[L-1]:
        L-=1
        left_reach=min(left_reach, cars[L]-oils[L])
        right_reach=max(right_reach, cars[L]+oils[L])
        change=True
    if R<n-1 and cars[R+1]<=right_reach:
        R+=1
        left_reach=min(left_reach, cars[R]-oils[R])
        right_reach=max(right_reach, cars[R]+oils[R])
        change=True
print(*range(L+1,R+2))