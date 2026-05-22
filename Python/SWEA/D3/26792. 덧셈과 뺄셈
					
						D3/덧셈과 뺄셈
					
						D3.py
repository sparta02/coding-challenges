T = int(input())

for test_case in range(T):
    x, y = map(int, input().split())

    A = (x + y) // 2
    B = (x - y) // 2

    print(A, B)