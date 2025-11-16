dirs = input()

# Please write your code here.
way=0
dx, dy= [0,1,0,-1], [1,0,-1,0]
x=0
y=0

for i in dirs:
    if i=="L":
        way=(way+3)%4
    elif i=="R":
        way=(way+1)%4
    elif i=="F":
        x=x+dx[way]
        y=y+dy[way]

print(x, y)

