n=int(input())
arr= [ input() for _ in range(n)]
arr=list(set(arr))
arr.sort(key=lambda x:(len(x), x))


for i in arr:
    print(i)
