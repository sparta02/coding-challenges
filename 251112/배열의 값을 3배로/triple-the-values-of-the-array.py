arr1 = [ list(map(int, input().split())) for _ in range(3)]

arr2 = [ 
    [ i*3 for i in row]
    for row in arr1
]

for i in range(3):
    for j in range(3):
        print(arr2[i][j], end=" ")
    print()