n = int(input())
a = list(input())
target = list(input())

# 0~num까지 숫자를 뒤집는 함수
def change_G_H(num):
    for i in range(num+1):
        if a[i]=='G':
            a[i]='H'
        else:
            a[i]='G'


result=0
# 문자 맨 끝부터 (n-1) 맨 앞까지(0) 탐색
for i in range(n-1, -1, -1):
    # 목표하는 문자와 다르다면 함수 호출
    if a[i]!=target[i]:
        change_G_H(i)
        result+=1
    # print(a)

print(result)