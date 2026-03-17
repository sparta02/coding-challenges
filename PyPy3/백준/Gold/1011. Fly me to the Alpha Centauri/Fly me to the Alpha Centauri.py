t=int(input())

for _ in range(t):
    a, b=map(int, input().split())
    target=b-a
    num=0
    i=0
    while target>num:
        i+=1
        num+=(i+1)//2
        
    print(i)
