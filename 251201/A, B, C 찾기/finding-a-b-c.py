arr = list(map(int, input().split()))


# 남은 수: A, B, C, A+B, B+C, A+C, A+B+C

# 1. 가장 작은 수: A
# 2. 가장 큰 수: A+B+C 제거
# 3. 이 2가지를 사용해 B+C 제거

A=min(arr)
arr.remove(A)

A_B_C=max(arr)
arr.remove(A_B_C)

arr.remove(A_B_C-A)


# 남은 수: B, C, A+B, A+C

# 4. 가장 작은 수: B
B=min(arr)
arr.remove(B)

# 남은 수: C, A+B, A+C
# 5. A+B 제거
arr.remove(A+B)

# 남은 수: C, A+C
# 6. 가장 작은 수: C
C=min(arr)


print(A, B, C)