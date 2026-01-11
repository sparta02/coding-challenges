K, N = map(int, input().split())

# Please write your code here.

num_list=[]
def call(num):
    if num==N+1:
        for item in num_list:
            print(item, end=" ")
        print()
        return
    for i in range(1,K+1):
        num_list.append(i)
        call(num+1)
        num_list.pop()

call(1)