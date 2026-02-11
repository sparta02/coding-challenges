n, m= map(int, input().split())

list=[]

def make_list(k):
    if k==m:
        for item in list:
            print(item, end=" ")
        print()
        return
    start_num=(list[-1] if len(list) else 0)+1
    for i in range(start_num, n+1):
        list.append(i)
        make_list(k+1)
        list.pop()

make_list(0)