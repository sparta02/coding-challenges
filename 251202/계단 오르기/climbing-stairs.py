MOD = 10007

n = int(input())

# 1. factorial과 inverse factorial 미리 계산 (MOD 10007)
fact = [1] * (n + 1)
inv_fact = [1] * (n + 1)

# factorial 계산
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD

# 페르마 소정리를 사용한 역팩토리얼 계산
# inv_fact[n] = fact[n]^(MOD-2) mod MOD
def mod_pow(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result

inv_fact[n] = mod_pow(fact[n], MOD - 2)

# 아래로 내려가며 inv_fact 계산
for i in range(n, 0, -1):
    inv_fact[i - 1] = (inv_fact[i] * i) % MOD


# 2. 조합 함수 (nCk)
def comb(a, b):
    if b < 0 or b > a:
        return 0
    return (fact[a] * inv_fact[b] % MOD) * inv_fact[a - b] % MOD


# 3. 가능한 모든 (2의 개수, 3의 개수) 조합에 대해 합산
answer = 0

for a in range(n // 2 + 1):   # a = 2의 개수
    remain = n - 2 * a
    if remain % 3 != 0:
        continue

    b = remain // 3           # b = 3의 개수

    # (a + b)! / (a! b!) = 조합(a+b, a)
    answer = (answer + comb(a + b, a)) % MOD

print(answer)
