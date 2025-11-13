n = int(input())

# Please write your code here.

def a(n):
    cnt=1
    for _ in range(n):
        for _ in range(n):
            if cnt==0:
                cnt+=1
            print(cnt%10, end=" ")
            cnt+=1
        print()

a(n)