n = int(input())

# 10개의 계단
# 2: 1번, 3: X
# 2: 2번, 3: 2번  4C2
# 2: 3번, 3: X
# 2: 4번, 3: X
# 2: 5번, 3: X


# 1. 팩토리얼 함수
def fact(n):
    result=1
    for i in range(1, n+1):
        result*=i
    return result


# 2. 2가 a번, 3이 b번 나올 때 나올 수 있는 경우의 수를 반환하는 calc

def calc(a, b):
    return int(fact(a+b)/(fact(a)*fact(b)))

# 3. 가능한 2, 3의 개수 조합을 찾아 calc를 호출하는 main 코드

count=0

for i in range(0, int(n/2)+1):
    num_two=i # 숫자 2의 개수
    temp_num= n-i*2
    if temp_num%3 !=0: # 만약 나머지 숫자가 3으로 나눠지지 않는다면 
        continue # 스킵
    num_three = int(temp_num/3) # 숫자 3의 개수

    # print(num_two, num_three)

    count+=calc(num_two, num_three)

print(count)