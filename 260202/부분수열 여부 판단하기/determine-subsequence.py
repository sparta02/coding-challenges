n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B가 A의 부분수열인지 확인
def check(A, B):
    i, j = 0, 0
    for j in range(m):
        # print(i, j)
        # print(A[i], B[j])
        
        while i<n and A[i]!=B[j]:
            i+=1
        if i==n:
            return False

    return True




if check(A,B):
    print("Yes")
else:
    print("No")