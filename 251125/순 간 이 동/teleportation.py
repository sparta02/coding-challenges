a, b, x, y = map(int, input().split())

# Please write your code here.
# a,b = min(a,b), max(a,b)

# x,y = min(x,y), max(x, y)

case_a=abs(b-a)
case_b=abs(a-x)+abs(y-b)
case_c=abs(a-y)+abs(x-b)
print(min(case_a,case_b,case_c))