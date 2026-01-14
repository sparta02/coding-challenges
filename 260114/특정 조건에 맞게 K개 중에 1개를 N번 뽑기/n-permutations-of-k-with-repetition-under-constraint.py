K, N = map(int, input().split())

# Please write your code here.
result=[]
def make_list(num):
    if num==N:
        for i in range(N):
            print(result[i], end=" ")
        print()
        return

    for i in range(1, K+1):
        if num>=2 and result[-2] == result[-1] and result[-1] == i:
            continue
        result.append(i)
        make_list(num+1)
        result.pop()

make_list(0)