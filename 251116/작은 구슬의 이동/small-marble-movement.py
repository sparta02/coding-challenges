n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
ways={
    "U":3,
    "R":0,
    "D":1,
    "L":2
}
pow=[r-1,c-1]
way=ways.get(d)
#print(pow)
#print(way)
dxs, dxy=[0,1,0,-1], [1,0,-1,0]

def check(a, b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

for i in range(t):
    if check(pow[0]+dxs[way], pow[1]+dxy[way]) == False:
        way=(way+2)%4
    else:
        pow[0]+=dxs[way]
        pow[1]+=dxy[way]
    #print(pow)

prin(pow[0]+1, pow[1]+1)