n, m = map(int, input().split())
list=[]

def choose(start, k):
    if k==m:
        for num in list:
            print(num, end=" ")
        print()
        return
    
    for i in range(start, n+1):
        list.append(i)
        choose(i, k+1)
        list.pop()


choose(1, 0)