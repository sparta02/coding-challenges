# 예시: n과 m을 입력받는 코드
import sys
n, m, a = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n)]
commands= list(map(int, input().split()))

def print_arr():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    print()
    
def one():
    for i in range(int(len(arr)/2)):
        for j in range(len(arr[0])):
            arr[i][j], arr[len(arr)-i-1][j]=arr[len(arr)-i-1][j], arr[i][j]
def two():
    for i in range(len(arr)):
        for j in range(int(len(arr[0])/2)):
            arr[i][j], arr[i][len(arr[0])-j-1]=arr[i][len(arr[0])-j-1], arr[i][j]
def three():
    four()
    four()
    four()

def four():
    global arr
    new_arr=[[0]*len(arr) for _ in range(len(arr[0]))]
    
    for i in range(len(arr[0])):
        for j in range(len(arr)): 
            new_arr[i][j]=arr[j][len(arr[0])-i-1]
    arr= [x[:] for x in new_arr]   

def five():
    global arr
    new_arr=[[0]*len(arr[0]) for _ in range(len(arr))]
    세로길이반=int(len(arr)/2)
    가로길이반=int(len(arr[0])/2)
    for i in range(세로길이반):
        for j in range(가로길이반):
            new_arr[i][j], new_arr[i][j+가로길이반], new_arr[i+세로길이반][j+가로길이반], new_arr[i+세로길이반][j]=arr[i+세로길이반][j],arr[i][j], arr[i][j+가로길이반], arr[i+세로길이반][j+가로길이반]
    arr= [x[:] for x in new_arr]  

def six():
    global arr
    new_arr=[[0]*len(arr[0]) for _ in range(len(arr))]
    세로길이반=int(len(arr)/2)
    가로길이반=int(len(arr[0])/2)
    for i in range(세로길이반):
        for j in range(가로길이반):
            new_arr[i][j], new_arr[i][j+가로길이반], new_arr[i+세로길이반][j+가로길이반], new_arr[i+세로길이반][j]=arr[i][j+가로길이반], arr[i+세로길이반][j+가로길이반], arr[i+세로길이반][j],arr[i][j]
    arr= [x[:] for x in new_arr]  
            
functions={
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six
}


for com in commands:
   functions[com]()
print_arr()
    