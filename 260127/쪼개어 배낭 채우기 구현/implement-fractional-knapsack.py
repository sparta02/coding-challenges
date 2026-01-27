N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
for i in range(N):
    v[i]/=w[i]

보석=[]

for i in range(N):
    보석.append((w[i],v[i]))

보석 = sorted(보석, key = lambda x: -x[1])
# print(보석)
result=0
for 무게, 가치 in 보석:
    # print(무게, 가치, M)
    if 무게>M:
        result+=M*가치
        break
    else:
        result+=무게*가치
        M-=무게

print(f"{result:.3f}")