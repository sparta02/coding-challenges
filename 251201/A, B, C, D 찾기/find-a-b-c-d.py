arr = list(map(int, input().split()))

# Please write your code here.

# A, B, C, D, A+B, B+C, C+D, A+C, B+D, A+D, A+B+C, A+B+D, A+C+D, B+C+D, A+B+C+D

#최소값: A
A=min(arr)
arr.remove(A)
#최대값: A+B+C+D
A_B_C_D=max(arr)
arr.remove(A_B_C_D)
#B+C+D 제거
arr.remove(A_B_C_D - A)

#B, C, D, A+B, B+C, C+D, A+C, B+D, A+D, A+B+C, A+B+D, A+C+D

#최소값 B
B=min(arr)
arr.remove(B)
#최대값 A+C+D
A_C_D=max(arr)
arr.remove(A_C_D)
#A+B 제거
arr.remove(A+B)
#C+D제거
arr.remove(A_C_D - A)
#A+B+C제거


#C, D, B+C, A+C, B+D, A+D, A+B+D, A+B+C
#최소값 C
C=min(arr)
#A+C+D에서 A+C빼기
D=A_C_D-A-C

print(A,B,C,D)